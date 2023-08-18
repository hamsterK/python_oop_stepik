class Scales:
    def __init__(self):
        self.right_scale = 0
        self.left_scale = 0

    def add_right(self, kg):
        self.right_scale += kg

    def add_left(self, kg):
        self.left_scale += kg

    def get_result(self):
        if self.left_scale == self.right_scale:
            return 'Весы в равновесии'
        elif self.left_scale < self.right_scale:
            return 'Правая чаша тяжелее'
        else:
            return 'Левая чаша тяжелее'
        