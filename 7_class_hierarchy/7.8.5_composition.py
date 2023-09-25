class Lecture:  # Классы Lecture и Conference🌶️
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = self.time_to_num(start_time)
        self.duration = self.time_to_num(duration)
        self.end_time = self.start_time + self.duration
        self.period = range(self.start_time, self.end_time)

    def time_to_num(self, s: str) -> int:
        h, m = map(int, s.split(':'))
        return h * 60 + m


class Conference:
    def __init__(self):
        self.timetable = []

    def add(self, lecture):
        for exist in self.timetable:
            if set(exist.period) & set(lecture.period):
                raise ValueError('Провести выступление в это время невозможно')
        self.timetable.append(lecture)
        self.timetable.sort(key=lambda lecture: lecture.start_time)

    def total(self):
        amount = sum(lecture.duration for lecture in self.timetable)
        return f'{amount // 60:02d}:{amount % 60:02d}'

    def longest_lecture(self):
        sabj = max(lecture.duration for lecture in self.timetable)
        return f'{sabj // 60:02d}:{sabj % 60:02d}'

    def longest_break(self):
        max_break = 0
        for i in range(len(self.timetable) - 1):
            max_break = max(self.timetable[i + 1].start_time - self.timetable[i].end_time, max_break)
        return f'{max_break // 60:02d}:{max_break % 60:02d}'


conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())
