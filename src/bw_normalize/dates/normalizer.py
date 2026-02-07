"""
Date normalization logic.
"""

from datetime import date, datetime

from ..exceptions import InvalidDateFormatError
from ..utils.validators import validate_locale

SUPPORTED_DATE_FORMATS = {
    "pt_BR": ["%d/%m/%Y", "%d-%m-%Y"],
    "en_US": ["%m/%d/%Y", "%m-%d-%Y"],
}


def normalize_date(value: str, locale: str = "pt_BR") -> date:
    """
    Normalize a date string to a date object.

    Args:
        value: Date value as string.
        locale: Locale identifier (e.g. 'pt_BR', 'en_US').

    Returns:
        datetime.date: Normalized date.

    Raises:
        InvalidDateFormatError: If date cannot be parsed.
    """
    validate_locale(locale, SUPPORTED_DATE_FORMATS.keys())

    if not isinstance(value, str):
        raise InvalidDateFormatError(
            f"Unsupported type for date normalization: {type(value)}"
        )

    for fmt in SUPPORTED_DATE_FORMATS[locale]:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    raise InvalidDateFormatError(
        f"Invalid date format for locale '{locale}': '{value}'"
    )
