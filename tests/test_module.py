import pytest

from package import module


@pytest.mark.parametrize("input, expected_output", [
    ("hi", "hi"),
    # add more tests here
])
def test_some_function(input, expected_output):
    assert module.some_function(input) == expected_output
