
import pytest

from app import calculate_bill


def test_calculate_bill():
    assert calculate_bill(10) == 60.0


def test_calculate_bill_with_custom_rate():
    assert calculate_bill(10, rate=8.0) == 80.0


def test_zero_units():
    assert calculate_bill(0) == 0.0


def test_negative_units_raise_error():
    with pytest.raises(ValueError, match="Units cannot be negative"):
        calculate_bill(-1)
