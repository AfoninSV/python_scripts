"""
Defines a Date class that:

-validates the day, month, and year of a date
-converts a date string in the format 'dd-mm-yyyy' to a Date object with corresponding day, month, and year attributes.
-The Date object can only be initialized via the from_string method
"""

class Date:
    """Representing a date object"""

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __repr__(self) -> str:
        return f"День: {self._day}\tМесяц: {self._month}\tГод: {self._year}"

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """
        Create a new Date object from a date string

        Raises:
            ValueError: if wrong date format
        :rtype: Date
        """
        if cls.is_date_valid(date):
            day, month, year = map(int, date.split(sep='-'))
            return Date(day, month, year)
        raise ValueError('Неверный формат даты, используйте формат dd-mm-yyyy')

    @staticmethod
    def is_date_valid(date: str) -> bool:
        lst_date = date.split('-')
        day, month, year = map(int, lst_date)

        if len(lst_date) != 3:
            return False
        elif (year < 1) or (month < 1) or (month > 12) or (day < 1) or (day > 31):
            return False
        return True
