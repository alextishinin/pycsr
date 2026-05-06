import pytest

from dev_practice.stats import mean


def test_mean_with_whole_numbers():
    assert mean([2, 4, 6, 8]) == 5


def test_mean_with_decimal_values():
    assert mean([1.5, 2.5, 3.5]) == pytest.approx(2.5)


def test_mean_with_empty_list_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        mean([])
