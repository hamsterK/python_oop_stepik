class Paragraph():
    def __init__(self, length):
        self._len = length
        self._s = ''
        self._right = False

    def add(self, s):
        self._s += f'{s} '

    def end(self):
        l = self._s.split()
        temp = l[0]
        for word in l[1:]:
            if len(temp) + len(word) + 1 <= self._len:
                temp += f' {word}'
            else:
                print(f'{(temp, temp.rjust(self._len))[self._right]}')
                temp = word
        if temp:
            print((temp, temp.rjust(self._len))[self._right])
        self._s = ''


class LeftParagraph(Paragraph):
    pass


class RightParagraph(Paragraph):
    def __init__(self, length):
        super().__init__(length)
        self._right = True


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()
