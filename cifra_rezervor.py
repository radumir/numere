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
