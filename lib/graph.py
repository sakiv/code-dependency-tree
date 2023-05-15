# System modules
import sys
import os
import mimetypes
import re

# 3rd party modules
import networkx as nx

# Local modules
from lib import utils

__regex = None
__ignoreList: list = []
__debugEnabled = False

def build_dependency_graph(path: str, regex: str, debugEnabled: bool = False):

    global __debugEnabled, __regex, __ignoreList
    __debugEnabled = debugEnabled
    __regex = utils.validate_regex(regex)

    if os.path.exists('.depignore'):
        with open('.depignore', 'r') as f:
            __ignoreList = f.read().splitlines()
            f.close()
    
    def process_folder(folderPath: str, level: int = 0):
        graph = nx.DiGraph()

        for item in os.listdir(folderPath):
            if item in __ignoreList:
                continue
            itemPath = os.path.join(folderPath, item)

            if os.path.isdir(itemPath):
                graph.add_edges_from(build_dependency_graph(itemPath, level+1))
            else:
                if __debugEnabled:
                    # print('####################################')
                    print('Processing file: {}'.format(itemPath))
                    print('File type: {}'.format(mimetypes.guess_type(itemPath)))
                    # print('####################################')

                data: str = utils.get_file_contents(itemPath)
                deps: list = __regex.findall(data)

                if not deps:
                    graph.add_node(item)
                    continue
                else:
                    for dep in set(deps):
                        graph.add_edge(item, dep)
                    __debugEnabled and print(graph.edges())
                    
        return graph

    def print_graph(graph: object):
        print('')
        print('-----------------')
        print('Dependency graph:')
        print('-----------------')
        print('')

        level = {}
        for dep, item in list(nx.edge_dfs(graph)):
            if dep not in level.keys():
                level[dep] = 0
                print('* {}'.format(dep))
            level[item] = level[dep] + 1
            print('  {delimiter}|- {name}'.format(
                                        delimiter='|  ' * level[dep],
                                        name=item))
        print('')


    graph: object = process_folder(path)
    print_graph(graph)
