# System modules
import sys
import os
import mimetypes
import re

# 3rd party modules
import networkx as nx

__regex = None
__ignoreList: list = []
__roots = set()
__graph = nx.DiGraph()
__debugEnabled = False

def build_dependency_tree(path: str, regex: str, debugEnabled: bool = False):

    global __debugEnabled
    __debugEnabled = debugEnabled

    validate_regex(regex)

    global __ignoreList
    if os.path.exists(os.path.join(path, '.depignore')):
        with open(os.path.join(path, '.depignore'), 'r') as f:
            __ignoreList = f.read().splitlines()
            f.close()
    
    graph: object = process_folder(path)
    return {
        'roots': __roots,
        'graph': __graph,
    }
    
    
def validate_regex(regex: str, escape: bool = False):
    global __regex
    try:
        __regex = re.compile(re.escape(regex)) if escape else re.compile(regex)
        return True
    except re.error:
        sys.exit('Err: Invalid regex - [{}]'.format(regex))

def process_folder(folderPath: str, level: int = 0):
    global __debugEnabled, __ignoreList, __graph
    depTree = {}

    for item in os.listdir(folderPath):
        if item in __ignoreList:
            continue
        itemPath = os.path.join(folderPath, item)
        isDir = os.path.isdir(itemPath)

        if os.path.isdir(itemPath):
            depTree[item] = build_dependency_tree(itemPath, level+1)
        else:
            if __debugEnabled:
                # print('####################################')
                print('Processing file: {}'.format(itemPath))
                print('File type: {}'.format(mimetypes.guess_type(itemPath)))
                # print('####################################')

            data: str = get_file_contents(itemPath)
            deps: list = __regex.findall(data)

            if not deps:
                __roots.add(item)
                continue
            else:
                __graph.add_edges_from(list(dict.fromkeys(deps, item).items()))
                depTree[item] = dict.fromkeys(deps)
                
    return depTree


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
            