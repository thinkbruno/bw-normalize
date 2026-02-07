import pytest
from decimal import Decimal

from bw_normalize.currency import normalize_currency
from bw_normalize.exceptions import InvalidCurrencyFormatError


def test_brazilian_currency_string():
    result = normalize_currency("R$ 1.234,56", "pt_BR")
    assert result == Decimal("1234.56")


def test_us_currency_string():
    result = normalize_currency("$1,234.56", "en_US")
    assert result == Decimal("1234.56")


def test_currency_from_float():
    result = normalize_currency(10.5)
    assert result == Decimal("10.5")


def test_currency_from_decimal():
    value = Decimal("99.99")
    result = normalize_currency(value)
    assert result == value


def test_invalid_currency_string():
    with pytest.raises(InvalidCurrencyFormatError):
        normalize_currency("invalid value")
