import pytest
import entrop
import time
import math
def test_frequency1():
    assert entrop.frequency1('AABBCC') == set(2,2,2)

def test_entropy_message_1():
    entropy_value = entrop.entrop('AABBCC')
    expected_value = 1.584962500721156
    assert  math.isclose(entropy_value, expected_value, abs_tol=0.0001)
