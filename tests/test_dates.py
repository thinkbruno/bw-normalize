import pytest
from datetime import date

from bw_normalize.dates import normalize_date
from bw_normalize.exceptions import InvalidDateFormatError


def test_brazilian_date_slash_format():
    result = normalize_date("31/12/2025", "pt_BR")
    assert result == date(2025, 12, 31)


def test_brazilian_date_dash_format():
    result = normalize_date("31-12-2025", "pt_BR")
    assert result == date(2025, 12, 31)


def test_us_date_format():
    result = normalize_date("12/31/2025", "en_US")
    assert result == date(2025, 12, 31)


def test_invalid_date_format():
    with pytest.raises(InvalidDateFormatError):
        normalize_date("2025-12-31")
