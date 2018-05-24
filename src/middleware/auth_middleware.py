import falcon


ALLOWED_UNAUTHENTICATED = {
    r'/': ['GET']
}


# To be customized later-on
class AuthMiddleware:

    def process_request(self, req, resp):

        req_path = req.path.lower()
        req_method = req.method.upper()
        if req_path in ALLOWED_UNAUTHENTICATED.keys() and \
                req_method in ALLOWED_UNAUTHENTICATED[req_path]:
            return

        # Perhaps, the request needs to be authenticated
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')

        challenges = ['Token type="Fernet"']

        if token is None:
            description = ('Please provide an auth token '
                           'as part of the request.')

            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

        if not self._token_is_valid(token, account_id):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, token, account_id):
        tokenized_list = str(token).strip().split(' ')

        if len(tokenized_list) == 2:
            if str(tokenized_list[0]).capitalize() == 'Bearer':
                return True  # Sure it is valid...

        return False

