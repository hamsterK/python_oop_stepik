class TextHandler:
    def __init__(self):
        self.words_list = list()

    def add_words(self, text):
        self.words_list.extend([word for word in text.split()])

    def get_shortest_words(self):
        return [word for word in self.words_list if len(word) == len(min(self.words_list, key=lambda x: len(x)))]

    def get_longest_words(self):
        return [word for word in self.words_list if len(word) == len(max(self.words_list, key=lambda x: len(x)))]