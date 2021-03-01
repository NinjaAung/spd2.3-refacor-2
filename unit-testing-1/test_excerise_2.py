from excerise_2 import get_age_carbon_14_dating
import pytest

def test_get_age_carbon_14_dating():
    assert get_age_carbon_14_dating(0.35) == 8680.34

def test_negative_get_age_carbon_14_dating():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(-1)

def test_zero_get_age_carbon_14_dating():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)
