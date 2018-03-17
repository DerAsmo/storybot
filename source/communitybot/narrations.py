# handle all narrations
# !use Threaded loop
import time

from communitybot.settings import DISCORD_HOOKS

from communitybot.steemi import steemi_post, steemi_comment, steemi_vote_up, steemi_get_votes
from communitybot.embeds import Webhook

from communitybot.anthology.index import StoryIndex


class Narrator:

    def __init__(self):
        self.index = StoryIndex()

        # all running narrations in a list
        self.narrations = self.get_active()

        self.sleeptime = 3

    # search for unfinished story posts on steem
    def get_active(self):
        narrations = []

        # TODO: find posts

        # TODO: check if finished

        # TODO: add to list

        return narrations

    def post_to_webhooks(self, narration, action):
        hook = Webhook(None)

        hook.add_field(
            name="Title",
            value=narration.get_title(),
        )

        if 'type' in action and action['type'] is not None:
            hook.add_field(
                name="Action Type",
                value=action['type'],
            )

        if 'value' in action and action['value'] is not None:
            hook.add_field(
                name="Action Value",
                value='\n'.join(action['value']),
                inline=True,
            )

        for hook_url in DISCORD_HOOKS:
            hook.url = hook_url
            hook.post()

    def process_actions(self, narration):
        actions = narration.get_actions()
        for action in actions:
            self.post_to_webhooks(narration, action)

            if action['type'] == 'post':
                postid = steemi_post(action['value'])
                narration.set_postid(postid)

            if action['type'] == 'comment':
                postid = steemi_comment(narration.get_postid(), action['value'])
                narration.add_comment(postid)

            if action['type'] == 'upvote':
                steemi_vote_up(action['value'])

            if action['type'] == 'getvotes':
                votes = steemi_get_votes(action['value'])
                narration.add_votes(action['value'], votes)

            if action['type'] == 'end':
                self.narrations.remove(narration)

    # update all narrations in the list
    def update_narrations(self):
        for narration in self.narrations:
            narration.update()
            self.process_actions(narration)

        if len(self.narrations) > 0:
            time.sleep(self.sleeptime)
            self.update_narrations()

    # start a new narration
    def start_narration(self, title=None):
        if title is not None:
            new_narration = self.index.get_story(title)

            if new_narration is not None:
                self.narrations.append(new_narration)
                new_narration.start()
                self.process_actions(new_narration)

        self.update_narrations()
