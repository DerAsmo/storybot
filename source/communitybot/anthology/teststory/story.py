# a single story

# ruleset

# reference to story entry post -> get / set

# update function - get response to story post (upvotes/comments/etc) and act accordingly

from os.path import dirname, join, abspath
from timeit import default_timer as timer
from communitybot.utils import build_postid, build_post

import communitybot.anthology.teststory


class Teststory:

    def __init__(self, duration=10):
        self.title = "a story to test"
        self.dirpath = dirname(abspath(communitybot.anthology.teststory.story.__file__))

        # user and permlink of first post
        self.username = None
        self.permlink = None

        # settings
        self.duration = duration

        self.timestart = None

        # contains a list of identifiers from comments important to the story
        self.comments = []

        # contains a list of votes
        # example [{'postid': postid, 'votes': [{'voter': 'username', ...}, ...]}, ...]
        self.votes = []
        # actions can be post, comment, upvote, getvotes
        # example [{'type': 'post', value: post}, ...]
        self.actions = []

    def set_postid(self, postid):
        self.username = postid['username']
        self.permlink = postid['permlink']

    def get_postid(self):
        postid = build_postid(self.username, self.permlink)
        return postid

    def add_comment(self, postid):
        self.comments.append(postid)

    def add_votes(self, postid, votes):
        votes = {'postid': postid, 'votes': votes}
        self.votes.append(votes)

    # helper function to guarantee all actions are the same
    def add_action(self, type, value=None):
        self.actions.append({'type': type, 'value': value})

    def get_actions(self):
        output = self.actions.copy()
        self.actions.clear()

        return output

    def get_title(self):
        return self.title

    # opens file with filename and returns its content
    def get_chapter(self, filename):
        filepath = join(self.dirpath, filename)
        file = open(filepath, 'r')
        output = file.read()
        file.close()

        return output

    # check if conditions are met to advance the story
    def update(self):
        timec = timer()
        durationc = timec - self.timestart

        if self.duration < durationc:

            title = 'RE: %s' % self.title
            body = self.get_chapter('endtext')
            post = build_post(title, body)

            self.add_action('comment', post)
            self.add_action('end')

        return self

    # start the story, create first post etc
    # basically the same as update but
    # - seperated in case there needs to be something done different at start
    # - there is no uid yet
    def start(self):
        self.timestart = timer()

        # obtain content of first post from file
        title = self.title
        body = self.get_chapter('starttext')
        post = build_post(title, body)

        self.add_action('post', post)

        return self
