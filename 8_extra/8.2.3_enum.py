from enum import Enum
from datetime import date, timedelta

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday.value
        self.after_today = after_today

    def date(self):
        days_until_next = (self.weekday - self.today.weekday()) % 7
        if not self.after_today and days_until_next == 0:
            days_until_next = 7  # Move to the next week
        next_date = self.today + timedelta(days=days_until_next)
        return next_date

    def days_until(self):
        next_date = self.date()
        days_until_next = (next_date - self.today).days
        return days_until_next


today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница

print(next_friday.date())
print(next_friday.days_until())
