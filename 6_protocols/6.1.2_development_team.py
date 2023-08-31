class DevelopmentTeam:
    def __init__(self):
        self.juniors = list()
        self.seniors = list()

    def add_junior(self, *args):
        self.juniors.extend(args)

    def add_senior(self, *args):
        self.seniors.extend(args)

    def __iter__(self):
        for dev in self.juniors:
            yield (dev, 'junior')
        for dev in self.seniors:
            yield (dev, 'senior')


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')
