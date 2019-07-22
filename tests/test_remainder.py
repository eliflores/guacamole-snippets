from math import remainder


def test_get_remainder():
    assert 10 % 4 == 2.0
    assert 12 % 3 == 0.0

    # New in version 3.7.
    assert remainder(10, 4) == 2.0
    assert remainder(12, 3) == 0.0
