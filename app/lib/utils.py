import datetime
import slugify

def add_metadata(document, update=False):

    ''' build a document to insert/update in the nosql db. '''

    date_now = datetime.datetime.now()

    document['author'] = 'alex' 
    document['permalink'] = slugify.slugify(document['title'])
    document['tags'] = [    tag.strip() 
                            for tag 
                            in document['tags'].split(',') ]
    document['last_edited'] = None

    if update:
        document['last_edited'] = date_now
    else:
        document['date_published'] = date_now

    return document


def get_short_text(file_content, max_chars=160):
    ''' this should be revised to include as many paragraphs that fit into 160 chars '''

    file_content = file_content.strip()

    short_text = ''
    walk_index = max_chars

    # content shorter than cut-off
    if len(file_content) < max_chars:
        short_text = file_content
    else:
        # cut-off point is on a space 
        if file_content[max_chars - 1] == ' ':
            short_text = ''.join(file_content[:max_chars])
        else:
            # cut-off point isn't a space. walk back until we find one or return empty string.
            while walk_index > -1 and file_content[walk_index] != ' ':
                walk_index -= 1
            short_text = ''.join(file_content[:walk_index])

    return short_text

def usage(msg=None, err=None):

    import sys

    if err:
        print "\nThe following errors occured:"
        print '\n\n'.join( ''.join(['  ' + e + '\n']) for e in err)
        sys.exit()
    msg = msg if msg else 'usage: publish <FILENAME>'
    print msg

def edit_in_vim(content):
    ''' 
      Takes text, writes to a temp file, opens the temp file with vim, you edit file in vim
      and save. Returns the saved text.
    ''' 

    import subprocess
    import tempfile

    with tempfile.NamedTemporaryFile(suffix='blogpost') as tempfile:
        tempfile.write(content.encode('utf-8'))
        tempfile.flush()
        subprocess.call(['vim', tempfile.name])
        text = open(tempfile.name, 'r').read().decode('utf-8')
        return text

