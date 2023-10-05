class HighScoreTable:
    def __init__(self, max_length):
        self.max_length = max_length
        self._scores = []

    @property # define a method as a getter for a class attribute,
    def scores(self):
        return self._scores

    def update(self, score):
        self._scores.append(score)
        self._scores.sort(reverse=True)
        self._scores = self._scores[:self.max_length]

    def reset(self):
        self._scores.clear()


high_score_table = HighScoreTable(3)

print(high_score_table.scores)    # []
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)    # [12, 10, 8]
