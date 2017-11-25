class CifraRezervor():
    def __init__(self):
        self.patrate = []
        for rand in [1, 2, 3]:
            for coloana in [1, 2, 3]:
                self.patrate.append(Patrat(rand, coloana))

    def deseneaza(self, x, y, tema):
        result = []
        for patrat in self.patrate:
            result += patrat.deseneaza(x, y, tema)
        return result


class Patrat():
    def __init__(self, rand, coloana):
        self.rand = rand
        self.coloana = coloana

    def x_absolut(self):
        return self.coloana - 1

    def y_absolut(self):
        return self.rand - 1

    def deseneaza(self, x, y, tema):
        result = []
        result += [self.coloreaza_patrat(x, y, tema)]
        result += [self.bordura_sus(x, y, tema)]
        result += [self.bordura_dreapta(x, y, tema)]
        result += [self.bordura_jos(x, y, tema)]
        result += [self.bordura_stanga(x, y, tema)]
        return result

    def coloreaza_patrat(self, x, y, tema):
        pass

    def bordura_sus(self, x, y, tema):
        # return ['line', x1, y1, x2, y2, color]
        pass

    def bordura_dreapta(self, x, y, tema):
        pass

    def bordura_jos(self, x, y, tema):
        pass

    def bordura_stanga(self, x, y, tema):
        pass
