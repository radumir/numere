import abs_coords
import constante_grafice


class CifraRezervor():
    def __init__(self, nr):
        self.nr = nr
        self.patrate = []
        for rand in [1, 2, 3]:
            for coloana in [1, 2, 3]:
                self.patrate.append(Patrat(self, rand, coloana))

    def deseneaza_rezervoare(self, x0, y0, tema):
        cabs = abs_coords.CoordonateAbsolute(x0, y0, tema[constante_grafice.cifra_rezervor__casuta_latura])
        result = []
        martor = 9
        for patrat in self.patrate:
            result += patrat.deseneaza(tema, cabs, result, self.nr >= martor)
            martor -= 1
        return result

    def deseneaza_ascuns(self, x0, y0, tema):
        cabs = abs_coords.CoordonateAbsolute(x0, y0, tema[constante_grafice.cifra_rezervor__casuta_latura])
        result = []
        for patrat in self.patrate:
            result += patrat.deseneaza(tema, cabs, result)
        return result

    def verifica(self, incercare):
        if incercare == self.nr:
            self.rezultat_corect()
        else:
            self.rezultat_gresit()

    def rezultat_corect(self):
        pass

    def rezultat_gresit(self):
        pass


class Patrat:
    def __init__(self, cifra_rezervor, rand, coloana):
        self.cifra_rezervor = cifra_rezervor
        self.rand = rand
        self.coloana = coloana

    def x1(self, cabs):
        return cabs.x(self.coloana - 1)

    def y1(self, cabs):
        return cabs.y(self.rand - 1)

    def x2(self, cabs):
        return cabs.x(self.coloana)

    def y2(self, cabs):
        return cabs.y(self.rand)

    def atins(self):
        self.cifra_rezervor.verifica(9 - (self.rand - 1) * 3 - (self.coloana - 1))

    def cheie_umplere_patrat(self, plin):
        if plin is None:
            return constante_grafice.cifra_rezervor__casuta_ascuns
        elif plin:
            return constante_grafice.cifra_rezervor__casuta_plin
        else:
            return constante_grafice.cifra_rezervor__casuta_gol

    def deseneaza(self, tema, cabs, acc, plin=None):
        self.coloreaza_patrat(tema, cabs, acc, plin)
        self.deseneaza_contur(tema, cabs, acc)

    def coloreaza_patrat(self, tema, cabs, acc, plin):
        cheie_culoare = self.cheie_umplere_patrat(plin)
        acc.append(['dreptunghi', self.x1(cabs), self.y1(cabs), self.x2(cabs), self.y2(cabs), tema[cheie_culoare]])
        if plin is None:
            acc.append(['zonaclick', self.x1(cabs), self.y1(cabs), self.x2(cabs), self.y2(cabs), self.atins])

    def deseneaza_contur(self, tema, cabs, acc):
        self.bordura_sus(tema, cabs, acc)
        self.bordura_dreapta(tema, cabs, acc)
        self.bordura_jos(tema, cabs, acc)
        self.bordura_stanga(tema, cabs, acc)

    def chei_bordura(self, test):
        if test:
            return constante_grafice.cifra_rezervor__bordura_exterioara__grosime, \
                constante_grafice.cifra_rezervor__bordura_exterioara__culoare
        return constante_grafice.cifra_rezervor__bordura_interioara__grosime, \
            constante_grafice.cifra_rezervor__bordura_interioara__culoare

    def bordura_sus(self, tema, cabs, acc):
        cheie_grosime, cheie_culoare = self.chei_bordura(self.rand == 1)
        acc.append(['linie', self.x1(cabs), self.y1(cabs), self.x2(cabs), self.y1(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_dreapta(self, tema, cabs, acc):
        cheie_grosime, cheie_culoare = self.chei_bordura(self.coloana % 3 == 0)
        acc.append(['linie', self.x2(cabs), self.y1(cabs), self.x2(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_jos(self, tema, cabs, acc):
        cheie_grosime, cheie_culoare = self.chei_bordura(self.rand == 3)
        acc.append(['linie', self.x1(cabs), self.y2(cabs), self.x2(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_stanga(self, tema, cabs, acc):
        cheie_grosime, cheie_culoare = self.chei_bordura(self.coloana % 1 == 0)
        acc.append(['linie', self.x1(cabs), self.y1(cabs), self.x1(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])
