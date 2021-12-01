from math_series.series import fibonacci
from math_series.series import lucas
import pytest

def test_import():
    assert fibonacci

def test_import():
    assert lucas

def test_fibonacci1():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_lucas1():
    actual = lucas(5)
    expected = 11
    assert actual == expected