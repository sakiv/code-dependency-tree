# System modules
import sys
import os
import re
# 3rd party modules

# Local modules
from lib import tree, graph, utils

formats = {
    'ksh': '/(\w+\.ksh)', 
    'js': '/(\w+\.js)'
}

typeMsg = 'Enter the type of dependency [options: tree, reverse-tree, graph, reverse-graph; default: tree]: '
srcMsg = 'Enter the path of folder or file [default: {}]: '

depType = sys.argv[1] if len(sys.argv) > 1 else input(typeMsg.format(os.curdir))
srcPath = sys.argv[2] if len(sys.argv) > 2 else input(srcMsg.format(os.curdir))
format = sys.argv[3] if len(sys.argv) > 3 else None
debugEnabled = len(sys.argv) > 4 and sys.argv[4] == 'True'

while format not in list(formats.keys()) and not type(utils.validate_regex(format)) :
    format = input('Enter the pre-defined formats [ksh | js] or custom regex: ')

if not srcPath:
    srcPath = os.curdir
else:
    if not os.path.exists(srcPath):
        sys.exit('Err: No file or directory exists at input path - [{}]'.format(srcPath))

if depType == 'graph':
    graph.build_dependency_graph(srcPath, formats[format] if format in formats.keys() else format, debugEnabled)
else:
    tree.build_dependency_tree(srcPath, formats[format] if format in formats.keys() else format, debugEnabled)


