# System modules
import sys
import os
import mimetypes
import re

# 3rd party modules
import networkx as nx

# Local modules
from lib import utils

class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

__debugEnabled = False
__regex = None
__ignoreList: list = []
__leafs: dict = {}

def build_dependency_tree(path: str, regex: str, debugEnabled: bool = False):

    global __debugEnabled, __regex, __ignoreList, __leafs
    __debugEnabled = debugEnabled
    __regex = utils.validate_regex(regex)

    if os.path.exists('.depignore'):
        with open('.depignore', 'r') as f:
            __ignoreList = f.read().splitlines()
            f.close()

    def process_folder(folderPath: str):

        for item in os.listdir(folderPath):
            if item in __ignoreList:
                continue
            itemPath = os.path.join(folderPath, item)

            if os.path.isdir(itemPath):
                build_dependency_tree(itemPath)
            else:
                if __debugEnabled:
                    # print('####################################')
                    print('Processing file: {}'.format(itemPath))
                    print('File type: {}'.format(mimetypes.guess_type(itemPath)))
                    # print('####################################')


                data: str = utils.get_file_contents(itemPath)
                deps: list = __regex.findall(data)

                parent = __leafs[item] if item in __leafs else Node(item)
                if item not in __leafs:
                    __leafs[item] = parent

                for dep in set(deps):
                    child = __leafs[dep] if dep in __leafs else Node(dep)                    
                    parent.add_child(child)
                    if dep not in __leafs:
                        __leafs[dep] = child
                    
        __debugEnabled and print(parent)
        return parent
    
    def traverse_tree(node, level=-1):        
        print('  {delimiter}|- {name}'.format(
                                                delimiter='|  ' * level,
                                                name=node.name)) if level >= 0 else print('* {}'.format(node.name))
        for child in node.children:
            traverse_tree(child, level+1)
        
        

    def build_tree(leafs: object):
        print('')
        print('-----------------')
        print('Dependency tree:')
        print('-----------------')
        print('')

        ancestors = set()
        for leaf in leafs.values():
            if not leaf.parents:
                ancestors.add(leaf)
        
        for ancestor in ancestors:
            traverse_tree(ancestor)
            print('')    
        print('')
                
    process_folder(path)    
    build_tree(__leafs)
