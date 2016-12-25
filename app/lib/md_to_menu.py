#!/usr/env/bin python

import sys

def md_to_menu(md):

    with open(sys.argv[1]) as f:

        lines = f.read().split('\n')
        headings = [ line 
                     for line in lines 
                     if line.strip().startswith('#') ] 


