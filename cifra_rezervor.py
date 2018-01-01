class CifraRezervor():
    def __init__(self):
        self.patrate = []
        for rand in [1, 2, 3]:
            for coloana in [1, 2, 3]:
                self.patrate.append(Patrat(rand, coloana))

    def deseneaza(self, tema):
        result = []
        for patrat in self.patrate:
            result += patrat.deseneaza(tema, result)
        return result


class Patrat():
    def __init__(self, rand, coloana):
        self.rand = rand
        self.coloana = coloana

    def x1(self):
        return self.coloana - 1

    def y1(self):
        return self.rand - 1

    def x2(self):
        return self.coloana

    def y2(self):
        return self.rand

    def deseneaza(self, tema, acc):
        self.coloreaza_patrat(tema, acc)
        self.deseneaza_contur(tema, acc)

    def coloreaza_patrat(self, tema, acc):
        pass

    def deseneaza_contur(self, tema, acc):
        self.bordura_sus(tema, acc)
        self.bordura_dreapta(tema, acc)
        self.bordura_jos(tema, acc)
        self.bordura_stanga(tema, acc)

    def bordura_sus(self, tema, acc):
        # return ['line', x1, y1, x2, y2, color]
        pass

    def bordura_dreapta(self, tema, acc):
        pass

    def bordura_jos(self, tema, acc):
        pass

    def bordura_stanga(self, tema, acc):
        pass
