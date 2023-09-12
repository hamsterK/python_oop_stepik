class TreeBuilder:
    def __init__(self):
        self._tree = []
        self._t = {}
        self.level = 0

    def __enter__(self):
        self._t.setdefault(self.level, []).append([])
        self.level += 1
        self._t[self.level] = self._t[self.level - 1][-1]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        if not self._t[self.level][-1]:
            self._t[self.level].pop()
        if self.level == 0:
            self._tree.extend(self._t[self.level])
            self._t.clear()

    def add(self, item):
        if self.level == 0:
            self._tree.append(item)
        else:
            self._t[self.level].append(item)

    def structure(self):
        return self._tree


tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass

print(tree.structure())
