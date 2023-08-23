import re


class StrExtension:

    @staticmethod
    def remove_vowels(string):
        return re.sub(r'[AEIOUYaeiouy]', '', string)

    @staticmethod
    def leave_alpha(string):
        return re.sub(r'[^A-Za-z]', '', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', char, string)


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
