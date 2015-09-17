#!/usr/bin/env python

import tempfile
from subprocess import call

content = 'abc'

with tempfile.NamedTemporaryFile(suffix='task') as tempfile:
    tempfile.write(content)
    tempfile.flush()
    call(['vim', tempfile.name])
    text = open(temp.name, 'r').read()
