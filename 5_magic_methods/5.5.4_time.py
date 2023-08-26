class Time:
    def __init__(self, hours, minutes):
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
        self.hours = hours % 24
        self.minutes = minutes

    def __str__(self):
        # {self.hours:02d} means "format self.hours as an integer with at least 2 digits,
        # padding with zeros if necessary
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            if self.minutes >= 60:
                self.hours += self.minutes // 60
                self.minutes = self.minutes % 60
            self.hours = self.hours % 24
            return self
        return NotImplemented


time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)

time1 += time2
print(time1)
