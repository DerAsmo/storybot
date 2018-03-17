from communitybot.anthology.teststory.story import Teststory


class StoryIndex:
    def __init__(self):
        # create a list of all stories contained inside directory
        self.stories = self.detect_stories()

    def detect_stories(self):
        # TODO: get list of directories
        # TODO: validate existing stories in directories
        return ['teststory']

    # return a list of available stories
    def get_stories(self):
        return self.stories

    # return handle to a single story
    def get_story(self, title):
        # TODO: start specified story, eg generic class?
        if title in self.stories:
            story = Teststory()
        else:
            story = None

        return story
