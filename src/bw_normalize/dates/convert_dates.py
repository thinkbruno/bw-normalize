from datetime import date, datetime
from enum import Enum
from typing import Callable


class DateFormat(Enum):
    BR = "br"
    FULL_BR = "full_br"
    FULL_US = "full_us"


class ConvertDates:
    """
    Responsible for converting ISO date strings (YYYY-MM-DD)
    into different human-readable formats.
    """

    def __init__(self, date_format: DateFormat):
        self._date_format = date_format
        self._formatters: dict[DateFormat, Callable[[date], str]] = {
            DateFormat.BR: self._format_br,
            DateFormat.FULL_BR: self._format_full_br,
            DateFormat.FULL_US: self._format_full_us,
        }

    def convert(self, value: str) -> str:
        """
        Converts an ISO date string (YYYY-MM-DD) into the configured format.
        """
        parsed_date = self._parse_date(value)

        formatter = self._formatters.get(self._date_format)
        if not formatter:
            raise ValueError(f"Date format '{self._date_format.value}' is not supported")

        return formatter(parsed_date)


    def _parse_date(self, value: str) -> date:
        if not isinstance(value, str):
            raise TypeError("Date value must be a string")

        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: '{value}'. Expected YYYY-MM-DD")


    def _format_br(self, value: date) -> str:
        return value.strftime("%d/%m/%Y")

    def _format_full_br(self, value: date) -> str:
        month_name = self._get_month_name(value.month, "br")
        return f"{value.day} de {month_name} de {value.year}"

    def _format_full_us(self, value: date) -> str:
        month_name = self._get_month_name(value.month, "us")
        day_suffix = self._get_day_suffix(value.day)
        return f"{month_name} {value.day}{day_suffix}, {value.year}"


    def _get_day_suffix(self, day: int) -> str:
        if 11 <= day <= 13:
            return "th"

        match day % 10:
            case 1:
                return "st"
            case 2:
                return "nd"
            case 3:
                return "rd"
            case _:
                return "th"

    def _get_month_name(self, month: int, locale: str) -> str:
        months = {
            "br": [
                "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
            ],
            "us": [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
        }

        try:
            return months[locale][month - 1]
        except (KeyError, IndexError):
            raise ValueError("Invalid month or locale")
