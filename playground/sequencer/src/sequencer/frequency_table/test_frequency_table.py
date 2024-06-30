from .frequency_table import *

def test_extractsfeatures():
    assert construct_frequency_table([1,0,1,1,1,0,1,1]) == FrequencyTable([[1,0],[0,0,0,1]], 8)

def test_roundtrip():
    original = [1,0,1,1,1,0,1,1]
    frequency_table = construct_frequency_table(original)
    assert list(frequency_table) == original