import os

def make_path(theme, resource_dirname):

    return os.path.abspath(os.path.join(os.path.relpath('themes'), theme, resource_dirname)) 

themes = {
    'default': {
        'static': make_path('default','static'), 
        'templates': make_path('default','templates') 
    },
    'new': {
        'static': make_path('new', 'static'),
        'templates': make_path('new', 'templates'),
    }
}
