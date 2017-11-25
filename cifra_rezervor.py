class CifraRezervor():
    def __init__(self):
        self.patrate = []
        for rand in [1, 2, 3]:
            for coloana in [1, 2, 3]:
                self.patrate.append(Patrat(rand, coloana))


class Patrat():
    def __init__(self, rand, coloana):
        self.rand = rand
        self.coloana = coloana

    def x_absolut(self):
        return self.coloana - 1

    def y_absolut(self):
        return self.rand - 1
