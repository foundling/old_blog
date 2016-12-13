import re
import sys

'''

    compile.py - Command-line script to merge Markdown with code snippets into a single file.
    
    compile <filepath> <code directory>

'''


def usage():

    '''

    compile.py usage:

    compile [/path/to/markdown_file] [/path/to/code_snippets] [/path/to/output/file] 

    '''
    
    print usage.__doc__

def get_extension(filepath):

    path = os.path.abspath(filepath)
    basename = os.path.basename(path) 

    if len(path.split('.')) < 2:
        return None

    return path.split('.')[-1] 

def merge(markdown_filepath=None, code_snippets=None, placeholder='%CODE%'):

    with open(markdown_filepath, 'r') as input_file:

        content = input_file.read() 
        matches = re.findall(delimiter)

        if len(matches) != len(code_snippets):
            raise ValueError('Your code snippet count should match your delimiter count but does not.')


if __name__ == '__main__':

    program, args = sys.argv[0], sys.argv[1:]

    if len(args) < 3:
        usage()
        sys.exit()

    output = merge(**kwargs);
    
    print(output)

