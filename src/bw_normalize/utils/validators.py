"""
Reusable validation helpers.
"""

from typing import Iterable

from ..exceptions import InvalidLocaleError


def validate_locale(locale: str, supported_locales: Iterable[str]) -> None:
    """
    Validate if the locale is supported.

    Args:
        locale: Locale identifier (e.g. 'pt_BR', 'en_US').
        supported_locales: Iterable of supported locale strings.

    Raises:
        InvalidLocaleError: If locale is not supported.
    """
    if locale not in supported_locales:
        raise InvalidLocaleError(f"Locale '{locale}' is not supported.")
