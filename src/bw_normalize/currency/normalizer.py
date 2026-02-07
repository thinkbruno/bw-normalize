"""
Currency normalization logic.
"""

import re
from decimal import Decimal, InvalidOperation
from typing import Union

from .locales import CURRENCY_LOCALES
from ..exceptions import InvalidCurrencyFormatError
from ..utils.validators import validate_locale


def normalize_currency(
    value: Union[str, float, Decimal],
    locale: str = "pt_BR"
) -> Decimal:
    """
    Normalize a monetary value based on locale rules.

    Args:
        value: Monetary value as string, float or Decimal.
        locale: Locale identifier (e.g. 'pt_BR', 'en_US').

    Returns:
        Decimal: Normalized monetary value.

    Raises:
        InvalidCurrencyFormatError: If value cannot be parsed.
    """
    validate_locale(locale, CURRENCY_LOCALES.keys())

    if isinstance(value, Decimal):
        return value

    if isinstance(value, (int, float)):
        return Decimal(str(value))

    if not isinstance(value, str):
        raise InvalidCurrencyFormatError(
            f"Unsupported type for currency normalization: {type(value)}"
        )

    config = CURRENCY_LOCALES[locale]

    try:
        cleaned = value.strip()

        # Remove currency symbol
        cleaned = cleaned.replace(config["symbol"], "").strip()

        # Remove thousand separators
        cleaned = cleaned.replace(config["thousand_separator"], "")

        # Replace decimal separator with dot
        cleaned = cleaned.replace(config["decimal_separator"], ".")

        return Decimal(cleaned)

    except (InvalidOperation, AttributeError):
        raise InvalidCurrencyFormatError(
            f"Invalid currency format: '{value}'"
        )
