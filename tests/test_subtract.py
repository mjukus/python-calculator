"""Test the subtract function from the pythoncalculator package"""
from pythoncalculator import subtract


def test_subtract():
    """Test that subtract returns correct result"""
    assert subtract(1, 3) == -2
