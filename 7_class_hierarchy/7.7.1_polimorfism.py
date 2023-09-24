from datetime import datetime


class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime(year, month, day)

    def format(self):
        return datetime.strftime(self.date, '%m-%d-%Y')

    def iso_format(self):
        return datetime.strftime(self.date, '%Y-%m-%d')


class ItalianDate(USADate):
    def format(self):
        return datetime.strftime(self.date, '%d/%m/%Y')


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())
