class Wordplay:
    def __init__(self, words=None):
        self.words = list(words) if words is not None else []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return [word for word in self.words if all(i in args for i in set(word))]

    def avoid(self, *args):
        return [word for word in self.words if all(arg not in set(args) for arg in word)]


wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))
