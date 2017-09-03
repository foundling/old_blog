import arrow
import urllib
import markdown

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

def md(mdText):

    return markdown.markdown(mdText, extensions=['markdown.extensions.toc'])

def md_toc(md):

    def parse(line):
        tag, content = line.strip().split(' ', 1)
        return ('\t'* (len(tag) - 1)) + '+ ' + content

    output = [  parse(line)
                for line in md.split('\n')
                if line.strip().startswith('#') ]

    print '\n'.join(['+ Table of Contents'] + output)
    return '\n'.join(['+ Table of Contents'] + output)


