import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, x, expected", [
    (0, 0, 5, 0, -3, 0),  # Testing horizontal line
    (1, 1, 2, 3, 3, 5),  # Testing line with postive slope
    (-5, 5, 0, 0, 8, -8)])  # Testnig line with negative slope
def test_y_on_line(x1, y1, x2, y2, x, expected):
    from on_line import y_on_line
    answer = y_on_line(x1, y1, x2, y2, x)
    assert answer == expected
