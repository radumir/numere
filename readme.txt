Program reprezentare numere ca si rezervoare
============================================

Fiecare cifra a numarului e reprezentata ca o cifra Sudoku.
E un rezervor mare compus din 9 rezervoare mai mici.
Cand e complet gol avem valoarea 0.
Cand numai rezervorul din dreapta jos e plin avem 1.
Cand rezervorul din dreapta jos si cel din stanga lui sunt pline avem 2.
Cand linia de jos e plina avem 3.
...
Cand toate rezervoarele sunt pline avem 9.
Cand apa creste in rezervorul mare la fel cresc si numerele.

Pentru desenare avem nevoie sa luăm de undeva elementele grafice.
Ele vor fi luate dintr-o temă - pe care o vom implementa folosind un dicționar.
Dar pentru a putea fi accesate avem nevoie de cheile de acces, de 'numele' valorilor
respective din temă.
Aceste nume vor servi ca element comun între partea de construire a comenzilor
de desenat - cifra_rezervor.py și modulul în care se va face efectiv desenarea
(care nu este încă implementat).
Pentru a nu gresi un nume in programul de desenare le vom introduce folosind un fisier
de constante - constante_grafice.py. Numele nu vor putea apartine decat setului
de constante definit in acel modul. In felul acesta nu vom putea face nicio greseala
de tastare (care va fi greu de depistat).
Vom desena patratele in coordonate relative.
Sistemul de coordonate va fi coltul din stanga sus a cifrei rezervor.
Unitatea va fi latura patratului.
Rezultatul desenarii va fi colectat intr-un acumulator, pentru a nu
construi de fiecare date o lista.
Anumite instructiuni se repeta de mai multe ori.
In cazul asta adaugarea unei metode in care izolam codul comun
constituie o imbunatatire a codului.


Sunt două moduri de afișare a unui pătrat. Cu rezervoarele la vedere,
și fără afișare rezervoare, pentru a putea alege un rezervor.
cifra_rezervor.deseneaza devine cifra_rezervor.deseneaza_rezervoare,
respectiv cifra_rezervor.deseneaza_ascuns.

Definit o metoda clicked pentru patrat in care se apeleaza metoda
verifica pt cifra_rezervor.
Codul care interpreteaza zonaclick la un click in zona delimitata
de x1,y1 si x2,y2 va apela metoda atins pentru patrat care
va apela metoda verifica pt cifra_rezervor.