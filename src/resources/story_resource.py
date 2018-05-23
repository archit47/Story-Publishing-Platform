import falcon


class StoryResource:

    def on_get(self, req, resp, story_id):
        return falcon.HTTP_200


class NewStoryResource:

    def on_post(self, req, resp):
        return falcon.HTTP_201