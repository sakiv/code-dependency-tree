# 3rd party modules
import networkx as nx

def print_tree(tree: object, level: int = 0):
    for item in tree:
        print('{}|- {}'.format('|  '*level, item))
        if isinstance(tree[item], dict):
            print_tree(tree[item], level+1)

def print_graph(graph: object, roots: set):
    print('')
    print('-----------------')
    print('Dependency graph:')
    print('-----------------')
    print('')

    for root in roots:
        level = {root: 0}
        print('* {}'.format(root))
        for dep, item in nx.dfs_edges(graph, root):
            level[item] = level[dep] + 1
            print('  {delimiter}|- {name}'.format(
                                        delimiter='|  ' * level[dep],
                                        name=item))
        print('')
    
    print('')
    