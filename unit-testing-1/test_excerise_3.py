from excerise_3 import calculate_stat
import pytest
import mock


@pytest.mark.parametrize("test_input,expected", [("string", ValueError), (True, ValueError), (123, ValueError),(0.123,ValueError)])
def test_non_list_calculate_stat(test_input, expected):
    with pytest.raises(expected):
        calculate_stat(test_input)


def test_zerored_calculate_stat():
    assert calculate_stat([0,0,0,0]) == (0.0,0.0)

def test_empty_calculate_stat():
    with pytest.raises(ZeroDivisionError):
        calculate_stat([])

def test_misc_calculate_stat():
    with pytest.raises(ValueError):
        calculate_stat([2,"1","c","!"])

def test_negative_calculate_stat():
    with pytest.raises(ValueError):
        calculate_stat([-1,-2,-3,-4])