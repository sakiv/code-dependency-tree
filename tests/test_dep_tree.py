from lib import processor, utils

def test_dep_tree_ksh():
    # Test that the dependency tree is built correctly
    # for a simple case
    result = processor.build_dependency_tree('./sample-data/ksh', '/(\w+\.ksh)')    
    assert type(result) is dict