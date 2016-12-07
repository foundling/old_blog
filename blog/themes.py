import os

def make_path(theme, resource_dirname):

    return os.path.abspath(os.path.join(os.path.relpath('themes'), theme, resource_dirname)) 

themes = {
    'default': {
        'static': make_path('default','static'), 
        'templates': make_path('default','templates') 
    },
    'test': {
        'static': make_path('test', 'static'),
        'templates': make_path('test', 'templates'),
    }
}
