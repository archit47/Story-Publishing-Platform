import uuid


class ContextMiddleware:

    def set_context(req, resp):
        if not req.context.get('request_id'):
            req.context['request_id'] = str(uuid.uuid4())

        # set a unique request-id for each request
        resp.set_header('request-id', req.context['request_id'])

    def process_request(self, req, resp):
        self.set_context(req, resp)

