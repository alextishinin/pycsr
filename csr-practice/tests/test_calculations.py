import pytest

from csr_practice.calculations import calculate_bmi


def test_calculate_bmi() -> None:
    assert calculate_bmi(70, 1.75) == pytest.approx(22.857142857142858)


def test_calculate_bmi_underweight() -> None:
    assert calculate_bmi(50, 1.75) < 18.5
