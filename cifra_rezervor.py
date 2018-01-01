import abs_coords
import constante_grafice


class CifraRezervor():
    def __init__(self):
        self.patrate = []
        for rand in [1, 2, 3]:
            for coloana in [1, 2, 3]:
                self.patrate.append(Patrat(rand, coloana))

    def deseneaza(self, x0, y0, tema):
        cabs = abs_coords.CoordonateAbsolute(x0, y0, tema[constante_grafice.cifra_rezervor__casuta_latura])
        result = []
        for patrat in self.patrate:
            result += patrat.deseneaza(tema, cabs, result)
        return result


class Patrat():
    def __init__(self, rand, coloana):
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

    def deseneaza(self, tema, cabs, acc):
        self.coloreaza_patrat(tema, cabs, acc)
        self.deseneaza_contur(tema, cabs, acc)

    def coloreaza_patrat(self, tema, cabs, acc):
        pass

    def deseneaza_contur(self, tema, cabs, acc):
        self.bordura_sus(tema, cabs, acc)
        self.bordura_dreapta(tema, cabs, acc)
        self.bordura_jos(tema, cabs, acc)
        self.bordura_stanga(tema, cabs, acc)

    def bordura_sus(self, tema, cabs, acc):
        if self.rand == 1:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_exterioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_exterioara__culoare
        else:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_interioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_interioara__culoare
        acc.append(['linie', self.x1(cabs), self.y1(cabs), self.x2(cabs), self.y1(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_dreapta(self, tema, cabs, acc):
        if self.coloana % 3 == 0:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_exterioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_exterioara__culoare
        else:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_interioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_interioara__culoare
        acc.append(['linie', self.x2(cabs), self.y1(cabs), self.x2(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_jos(self, tema, cabs, acc):
        if self.rand == 3:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_exterioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_exterioara__culoare
        else:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_interioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_interioara__culoare
        acc.append(['linie', self.x1(cabs), self.y2(cabs), self.x2(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])

    def bordura_stanga(self, tema, cabs, acc):
        if self.coloana % 1 == 0:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_exterioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_exterioara__culoare
        else:
            cheie_grosime = constante_grafice.cifra_rezervor__bordura_interioara__grosime
            cheie_culoare = constante_grafice.cifra_rezervor__bordura_interioara__culoare
        acc.append(['linie', self.x1(cabs), self.y1(cabs), self.x1(cabs), self.y2(cabs), tema[cheie_grosime], tema[cheie_culoare]])
