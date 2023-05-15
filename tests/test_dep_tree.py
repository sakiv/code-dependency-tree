from lib import tree

def test_dep_tree_ksh():
    # Test that the dependency tree is built correctly
    # for a simple case
    result = tree.build_dependency_tree('./sample-data/ksh', '/(\w+\.ksh)')    
    assert result is None