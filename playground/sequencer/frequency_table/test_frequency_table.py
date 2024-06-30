from unittest.test.test_assertions import *
from .frequency_table import *

def test_extractsfeature():
    expected = FrequencyTable([[1,0]], 4)
    assert construct_frequency_table([1,0,1,0]) == expected
