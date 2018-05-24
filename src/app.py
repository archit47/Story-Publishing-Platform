import falcon
from resources import (
    BaseResource,
    AuthorResource, NewAuthorResource,
    DraftResource, NewDraftResource, DraftsListResource,
    StoryResource, NewStoryResource,
    UserFeedResource
)
from middleware import (
    ContextMiddleware, AuthMiddleware
)
from errors import api_error_handler
from waitress import serve
from settings import HOST, PORT
from wsgiref import simple_server


# List of middleware
middleware_list = [
    ContextMiddleware(),
    AuthMiddleware()
]
# App instance
app = falcon.API(middleware=middleware_list)

# adding api routes below

app.add_route('/', BaseResource())

app.add_route('/author/{author_id:int}', AuthorResource())
app.add_route('/author', NewAuthorResource())
app.add_route('/author/{author_id:int}/draft/{draft_id:int}', DraftResource())
app.add_route('/author/{author_id:int}/draft', NewDraftResource())
app.add_route('/author/{author_id:int}/drafts', DraftsListResource())
app.add_route('/story/{story_id:int}', StoryResource())

# To publish a draft -> to convert a draft into a story
app.add_route('/story', NewStoryResource())

# To provide a list of stories for the user(author) -> populate reader's feed
app.add_route('/author/{author_id:int}/stories', UserFeedResource())

# add error-handler
app.add_error_handler(Exception, handler=api_error_handler)


if __name__ == "__main__":
    print("Hello World!")
    print("Server started listening on: %s:%s" % (HOST, PORT))
    # serve(app=app, host=HOST, port=PORT)
    web_server = simple_server.make_server(HOST, int(PORT), app)
    web_server.serve_forever(poll_interval=0.2)

