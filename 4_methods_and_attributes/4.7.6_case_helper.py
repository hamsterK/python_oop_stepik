import re


class CaseHelper:

    @staticmethod
    def is_snake(string):
        return bool(re.fullmatch(r'[a-z]+(_[a-z]+)*', string))

    @staticmethod
    def is_upper_camel(string):
        return bool(re.fullmatch(r'([A-Z][a-z]+)+', string))

    @staticmethod
    def to_snake(string):
        return re.sub(r'\B([A-Z])\B', r'_\1', string).lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())


print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.to_snake('BeeGeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
