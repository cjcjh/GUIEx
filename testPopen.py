# !/usr/bin/python

import os, sys

# using command mkdir
a = 'dir/w'

b = os.popen(a,'r',1)

print(b.read())