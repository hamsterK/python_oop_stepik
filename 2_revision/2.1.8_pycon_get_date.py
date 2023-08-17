"""
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.

Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.

Формат входных данных
На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.

Формат выходных данных
Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат
в формате DD.MM.YYYY.
"""

import calendar
import datetime

x = datetime.datetime(2020, 5, 17)

year, month = [int(input()) for i in range(2)]
dates = calendar.monthcalendar(year, month)

if dates[0][3] == 0:
    print(datetime.datetime(year, month, dates[4][3]).strftime("%d.%m.%Y"))
else:
    print(datetime.datetime(year, month, dates[3][3]).strftime("%d.%m.%Y"))

# 2012
# 3
