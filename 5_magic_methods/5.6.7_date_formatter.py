from datetime import datetime


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        dates_formats = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"
        }
        return datetime.strftime(d, dates_formats[self.country_code])


ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))
