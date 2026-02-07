"""
Custom exceptions.
"""


class NormalizeError(Exception):
    """Base exception for all bw-normalize errors."""
    pass


class InvalidLocaleError(NormalizeError):
    """Raised when an unsupported locale is provided."""
    pass


class InvalidCurrencyFormatError(NormalizeError):
    """Raised when a currency value cannot be parsed."""
    pass


class InvalidDateFormatError(NormalizeError):
    """Raised when a date value cannot be parsed."""
    pass
