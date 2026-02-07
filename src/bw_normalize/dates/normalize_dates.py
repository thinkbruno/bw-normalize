import re
from datetime import datetime, date


class NormalizeDates:
    """
    Responsible for normalizing multiple human-readable date formats
    into ISO format (YYYY-MM-DD).
    """

    _MONTHS = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12,
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12,
    }

    _ORDINAL_SUFFIXES = ("st", "nd", "rd", "th")

    # ========= PUBLIC API =========

    def normalize(self, value: str) -> str:
        """
        Normalizes a date string into ISO format (YYYY-MM-DD).
        """
        parsed_date = self._parse_date(value)
        return parsed_date.strftime("%Y-%m-%d")


    def _parse_date(self, value: str) -> date:
        if not isinstance(value, str):
            raise TypeError("Date value must be a string")

        value = value.strip().lower()

        parsers = [
            self._parse_iso,
            self._parse_dmy_dash,
            self._parse_dmy_slash,
            self._parse_full_pt,
            self._parse_full_en,
        ]

        for parser in parsers:
            result = parser(value)
            if result:
                return result

        raise ValueError(f"Unsupported or invalid date format: '{value}'")


    def _parse_iso(self, value: str) -> date | None:
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None

    def _parse_dmy_dash(self, value: str) -> date | None:
        try:
            return datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            return None

    def _parse_dmy_slash(self, value: str) -> date | None:
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            return None

    def _parse_full_pt(self, value: str) -> date | None:
        match = re.match(
            r"(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})",
            value
        )
        if not match:
            return None

        day, month_name, year = match.groups()
        month = self._MONTHS.get(month_name)

        if not month:
            return None

        return self._safe_date(year, month, day)

    def _parse_full_en(self, value: str) -> date | None:
        match = re.match(
            r"([a-z]+)\s+(\d{1,2})(st|nd|rd|th),\s*(\d{4})",
            value
        )
        if not match:
            return None

        month_name, day, _, year = match.groups()
        month = self._MONTHS.get(month_name)

        if not month:
            return None

        return self._safe_date(year, month, day)


    def _safe_date(self, year, month, day) -> date | None:
        try:
            return date(int(year), int(month), int(day))
        except ValueError:
            return None
