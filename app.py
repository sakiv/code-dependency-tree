# System modules
import sys
import os

# 3rd party modules

# Local modules
from lib import processor, utils

formats = {
    'ksh': '/(\w+\.ksh)', 
    'js': '/(\w+\.js)'
}

srcPath = sys.argv[1] if len(sys.argv) > 1 else input('Enter the path of folder or file [default: {}]: '.format(os.curdir))
format = sys.argv[2] if len(sys.argv) > 2 else None
debugEnabled = sys.argv[3] if len(sys.argv) > 3 else False

while format not in list(formats.keys()):
    format = input('Enter the path of folder or file [ksh | js]: ')

if not srcPath:
    srcPath = os.curdir
else:
    if not os.path.exists(srcPath):
        sys.exit('Err: No file or directory exists at input path - [{}]'.format(srcPath))

result = processor.build_dependency_tree(srcPath, formats[format])
utils.print_graph(result['graph'], result['roots'])

