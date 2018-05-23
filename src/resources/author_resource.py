import falcon


class AuthorResource:

    def on_get(self, req, resp, author_id):
        return falcon.HTTP_200

    def on_put(self, req, resp, author_id):
        return falcon.HTTP_202


class NewAuthorResource:

    def on_post(self, req, resp):
        return falcon.HTTP_201

