import re
from enum import Enum
from typing import Callable


class Locale(Enum):
    PT_BR = "pt_BR"
    EN_US = "en_US"


class NormalizeCurrency:
    """
    Responsible for:
    - Normalizing currency strings (str → float)
    - Formatting numeric values into currency strings (float → str)
    """

    def __init__(self, locale: Locale = Locale.PT_BR):
        self._locale = locale
        self._formatters: dict[Locale, Callable[[float, bool], str]] = {
            Locale.PT_BR: self._format_brl,
            Locale.EN_US: self._format_usd,
        }

    def normalize(self, value: str) -> float:
        """
        Converts a currency string into a float.

        Examples:
        - 'R$ 5.000,00' → 5000.0
        - '$5,000.00' → 5000.0
        """
        if not isinstance(value, str):
            raise TypeError("Currency value must be a string")

        cleaned_value = self._clean_currency_string(value)

        try:
            return float(cleaned_value)
        except ValueError:
            raise ValueError(f"Invalid currency format: '{value}'")

    def format(self, value: float, with_symbol: bool = True) -> str:
        """
        Formats a numeric value into a localized currency string.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")

        formatter = self._formatters.get(self._locale)
        if not formatter:
            raise ValueError(f"Locale '{self._locale.value}' is not supported")

        return formatter(float(value), with_symbol)


    def _format_brl(self, value: float, with_symbol: bool) -> str:
        format_pattern = "R$ {:,.2f}" if with_symbol else "{:,.2f}"
        formatted = format_pattern.format(value)

        return (
            formatted
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    def _format_usd(self, value: float, with_symbol: bool) -> str:
        format_pattern = "$ {:,.2f}" if with_symbol else "{:,.2f}"
        return format_pattern.format(value)


    def _clean_currency_string(self, value: str) -> str:
        """
        Removes currency symbols and normalizes decimal separators.
        """
        value = value.strip()

        # Remove currency symbols and spaces
        value = re.sub(r"[R$\s]", "", value)

        # Detect Brazilian decimal pattern (comma as decimal separator)
        if re.search(r",\d{2}$", value):
            value = value.replace(".", "").replace(",", ".")
        else:
            value = value.replace(",", "")

        return value
