def get_short_text(file_content, max_chars=160):
    ''' this should be revised to include as many paragraphs that fit into 160 chars '''

    return file_content.split('\n')[0] 

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

