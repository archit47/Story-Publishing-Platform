import falcon


class DraftResource:

    def on_get(self, req, resp, author_id, draft_id):
        return falcon.HTTP_200

    def on_put(self, req, resp, author_id, draft_id):
        return falcon.HTTP_202

    def on_delete(self, req, resp, author_id, draft_id):
        return falcon.HTTP_204


class NewDraftResource:

    def on_post(self, req, resp, author_id):
        return falcon.HTTP_201


class DraftsListResource:

    def on_get(self, req, resp, author_id):
        return falcon.HTTP_200


