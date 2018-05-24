class BaseResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        info = {
            'author': 'Archit Kapoor',

            'github_user': 'archit47',

            'profile_link': 'https://github.com/archit47',

            'repo_link': ('https://github.com/archit47/'
                          'Story-Publishing-Platform'),

            'problem_statement_link': ('https://github.com/91paisa/'
                                       'full-stack-developer-challenge')
        }

        resp.media = info

