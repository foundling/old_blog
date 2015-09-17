import sys
def usage(msg=None, err=None):
    if err:
        print "\nThe following errors occured:"
        print '\n\n'.join( ''.join(['  ' + e + '\n']) for e in err)
        sys.exit()
    msg = msg if msg else 'usage: publish <FILENAME>'
    print msg
