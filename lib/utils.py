import sys
import re

# 3rd party modules
import networkx as nx

def validate_regex(regex: str, escape: bool = False):
    try:
        return re.compile(re.escape(regex), re.IGNORECASE) if escape else re.compile(regex, re.IGNORECASE)        
    except re.error:
        sys.exit('Err: Invalid regex - [{}]'.format(regex))

def print_tree(tree: object, level: int = 0):
    for item in tree:
        print('{}|- {}'.format('|  '*level, item))
        if isinstance(tree[item], dict):
            print_tree(tree[item], level+1)

def get_file_contents(filePath: str):
    with open(filePath, 'r') as f:
        try:
            fileContent = f.read()
        except UnicodeDecodeError:
            global __debugEnabled
            __debugEnabled and print('Err: UnicodeDecodeError - {}'.format(filePath))
            fileContent = ''
        f.close()
        return fileContent