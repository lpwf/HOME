import pytest
from home2 import major_and_minor_elem


@pytest.mark.parametrize(
    "list,letter",
    [
        ([2, 2, 1, 1, 1, 2, 2], (2, 1))
    ],
)
def test_major_and_minor_elem(list, letter):
    result = major_and_minor_elem(list)
    assert result == letter
