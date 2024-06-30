from .run_list import *

def test_createsruns():
    assert construct_run_list([1,1,1,0,0,1]) == RunList([3,5,6])

def test_roundtrip():
    original = [0,0,0,1,1,0,1,1,0,0]
    run_list = construct_run_list(original)
    assert list(run_list) == original