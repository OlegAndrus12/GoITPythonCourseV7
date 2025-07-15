

class Date:
    MIN_YEAR = 1900

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_eu_format_dash(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)
    
    @classmethod
    def from_eu_format_slash(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

    @classmethod
    def update_min_year(cls, value):
        cls.MIN_YEAR = value
    
    @staticmethod
    def is_valid_date(date_as_string):
        day, month, _ = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12



Date.from_eu_format_dash("")

d = Date(12,31, 2)
print(d.MIN_YEAR)
d2 = d.from_eu_format_dash("11-12-3")
d2.update_min_year(2000)
print(d.MIN_YEAR)

