import falcon


class UserFeedResource:

    def on_get(self, req, resp, author_id):
        return falcon.HTTP_200

