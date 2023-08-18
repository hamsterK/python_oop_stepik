class Gun:
    def __init__(self):
        self.counter = 0

    def shoot(self):
        if self.counter % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.counter += 1

    def shots_count(self):
        return self.counter

    def shots_reset(self):
        self.counter = 0
