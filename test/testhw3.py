import pytest
from homewk3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "file,list",
    [
        ('../LIVE.txt', [(1, 5), (1, 9), (2, 4), (-1, 0), (1, 1), (3, 8)])
    ],
)
def test_find_maximum_and_minimum(file: str, list):
    result = find_maximum_and_minimum(file)
    assert result == list
