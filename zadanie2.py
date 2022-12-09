"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 2"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela, pagerank, potegowa
import numpy as np

class Zadanie2:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        self.nn = 200
        self.norma = 2
        
    def testy(self):
        """Testy wstepne"""
        ## wykonuje testy dla rożnych ilości iteracji
        testowe_ilosci_iteracji = [50, 400, 700]
        for ilosc_iteracji in testowe_ilosci_iteracji:
            # okreslam uklad rownan
            p1 = pagerank.PageRank(self.nn)
            # losujemy uklad
            print(f"\nTest dla ilosc_iteracji = {ilosc_iteracji}")
            p1.losuj()
            # przygotuje do iteracji
            p1.przygotuj_do_iteracji()
            # rozwiazuje uklad z wykorzystaniem metody iteracji Seidela
            seidel1 = iteracjaseidela.IteracjaSeidela(ukl = p1.v)
            potegowa1 = potegowa.Potegowa(ukl = p1.v)
            # wyznaczam macierz D i wektor C
            seidel1.przygotuj()
            
            # wykonuje iteracje używając metody iteruj dla iteracji Seidela
            iteracja_seidela1 = seidel1.iteruj(ilosc_iteracji, self.norma)
            niedokladnosc_seidela1 = seidel1.sprawdz_rozwiazanie(self.norma)
            print(f"Niedokładkość iteracji Seidela: {niedokladnosc_seidela1}")

            # wykonuje iteracje dla metody potęgowej uzywając metody iteruj
            iteracja_potegowa = potegowa1.iteruj(ilosc_iteracji,)
            niedokladnosc_potegowa1 = potegowa1.sprawdz_rozwiazanie(self.norma)







        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracji prostej"""
        # ustalam zbior parametrow
        # zmieniam je w równych odstępach
        param = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
        # okreslam uklad rownan
        p1 = pagerank.PageRank(self.nn)
        # dla kazdej wartosci parametru przeprowadzam po k testow
        # i wyswietlam wartosci wybranych charakterystyk eksperymentu
        sr_liczba_linkow_na_stronie = []
        sr_niedokladnosc_seidela = []
        sr_niedokladnosc_potegowa = []
        for ilosc_iteracji in param:
            liczba_linkow_na_stronie = 0.0
            niedokladnosc_seidela = 0.0
            niedokladnosc_potegowa = 0.0
            iteracje = 0
            while iteracje < self.k:
                # losujemy uklad
                p1.losuj()
                p1.przygotuj_do_iteracji()

                seidel = iteracjaseidela.IteracjaSeidela(ukl = p1.v)
                potegowa1 = potegowa.Potegowa(ukl = p1.v)

                seidel.przygotuj()   
                
                # wykonuje iteracje Seidela używając metody iteruj
                iteracja_seidela = seidel.iteruj(ilosc_iteracji, self.norma)
                jedna_niedokladnosc_seidela = seidel.sprawdz_rozwiazanie(self.norma)

                iteracja_potegowa = potegowa1.iteruj(ilosc_iteracji,)
                jedna_niedokladnosc_potegowa = potegowa1.sprawdz_rozwiazanie(self.norma)
                if iteracja_seidela == 0:
                    # jezeli nie mozna bylo wykonac iteracji
                    # nalezy powtorzyc pomiar
                    continue
                else:
                    # jezeli eksperyment udalo sie przeprowadzic
                    # agregujemy charakterystyki
                    niedokladnosc_seidela += jedna_niedokladnosc_seidela
                    niedokladnosc_potegowa += jedna_niedokladnosc_potegowa
                    liczba_linkow_na_stronie += p1.srednia_liczba_linkow()
                    iteracje += 1
            # obliczam srednie wartosci charakterystyk
            sr_liczba_linkow_na_stronie.append(liczba_linkow_na_stronie/self.k)
            sr_niedokladnosc_seidela.append(niedokladnosc_seidela/self.k)
            sr_niedokladnosc_potegowa.append(niedokladnosc_potegowa/self.k)
        # wypisujemy srednie charakterystyki
        print("Liczba iteracji\t\tLiczba linkow\t\tNiedokladnosc Seidela\t\tNiedokladnosc potegowa")
        print("------"*9)
        for i in range(len(param)):
            wyniki = f"{param[i]} \t\t\t"
            wyniki += f"{sr_liczba_linkow_na_stronie[i]:.6f} \t\t"
            wyniki += f"{sr_niedokladnosc_seidela[i]:.6e} \t\t\t"
            wyniki += f"{sr_niedokladnosc_potegowa[i]:.6e} \n"
            print(wyniki)
        
        

zad1 = Zadanie2()
zad1.testy()
zad1.badaj_zbieznosc()
