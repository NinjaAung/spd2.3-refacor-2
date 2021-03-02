from excerise_4 import extract_position
import pytest

@pytest.mark.parametrize("test_input,expected",[("Debug",None),("error",None),("Update Debug",None),("x:","")])
def test_keyword_extract_position(test_input,expected):
    assert extract_position(test_input) == expected

