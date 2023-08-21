class HourClock:
    def __init__(self, hours):
        if hours not in range(1, 13) or type(hours) is not int:
            raise ValueError('Некорректное время')
        else:
            self._hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, new_hours):
        if new_hours not in range(1, 13) or type(new_hours) is not int:
            raise ValueError('Некорректное время')
        else:
            self._hours = new_hours

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)
