# storybot
Storybot is a steem bot written in Python.
It's purpose is to automatically respond to user interactions.
Therefor it has to read data from the blockchain and post comments etc. accordingly.

## installation

For storybot to work it needs a working [Python](https://www.python.org/) with [steem-python](https://github.com/steemit/steem-python) packages.

You can download the repository using [Git](https://git-scm.com/):

``$git clone https://github.com/derasmo/storybot``

Modify settings.py within communitybot directory and add:
* login credentials for the Steem Account the bot meant to post with
* discord app token for the bot to receive commands via discord
* discord webhook for the bot to respond to discord

Start the bot by using:

``python storybot.py --run narration`` - for no discord integration, starting a predefined story

``python storybot.py --run discordbot`` - enabling commands and responses through discord

## how it works
Storybot provides a way to simply add new stories.

Stories can be added in anthology subdirectory.

## Actions

A Story can use actions that will be processed by the Narrator.
Add an action by using ``self.add_action(type, value)``.

### post

Sets up the root post of Story.
A post needs a title and content body.

Use ``build_post(title, content)`` to create a post item and pass it as value.

### comment

Create a comment on the root post.
A comment needs a title and content body.

Use ``build_post(title, content)`` to create a post object and pass it as value.

### upvote

Votes up a post or comment.
The value requires a postid.

For the root post username is set in self.username and permlink can be obtained through ``self.permlink``.
The postid of all associated comments is stored in a list accessed with ``self.comments``.

Use ``build_postid(username, permlink)`` to create a postid object and pass it as value.

### getvotes

Receive votes on the root post or comment.
The value requires a postid to deliver a result.

For the root post username is set in self.username and permlink can be obtained through ``self.permlink``.
The postid of all associated comments is stored in a list accessed with ``self.comments``.

Use ``build_postid(username, permlink)`` to create a postid object and pass it as value.

### end

Tells the Narrator the Story is ended.
Removes the story from the list of active stories.
