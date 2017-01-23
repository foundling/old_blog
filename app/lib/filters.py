import arrow
import urllib

def human_readable_date(datetime_object):

    ''' Takes an arrow.now().datetime object and returns a .humanize() version.'''

    return arrow.Arrow.fromdatetime(datetime_object).humanize() if datetime_object else ''

def clean_date(datetime_object):

    ''' Takes an arrow.now().datetime object and returns a .formatted version. '''

    return arrow.Arrow.fromdatetime(datetime_object).format('MM-DD-YYYY') if datetime_object else ''

def urlencode(qs):
    encoded = urllib.urlencode({ 'query': qs })
    return encoded.split('=')[1]

def urldecode(qs):
    decoded = urllib.unquote_plus({ 'query': qs }) 
    return decoded.split('=')[1]
