"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np
import matplotlib.pyplot as plt

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        self.n = 100          # wymiar macierzy
        self.norma = 0        # bede wykorzystywal norme wierszową
        self.epsilon = 1e-10
        
    def testy(self):
        """Testy wstepne"""
                    ### test dla alpha = 0.1
        alfa1 = 0.1
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar = self.n)
        # losujemy uklad
        u1.losuj_uklad_symetryczny_dodatnio_okreslony(alfa1)
        # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
        test1 = iteracjaprosta.IteracjaProsta(ukl = u1)
        # wyznaczam macierz D i wektor C
        test1.przygotuj()
        # wykonuje iteracje używając metody iteruj_twierdzenie
        iter1 = test1.iteruj_twierdzenie(
            eps = 1e-10,
            norma = self.norma,
            wyswietlaj = 0)
        seria1 = test1.normy.copy()
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)


                    ### test dla alpha = 0.5
        alfa2 = 0.5
        # okreslam uklad rownan
        u2 = uklad.Uklad(wymiar = self.n)
        # losujemy uklad
        u2.losuj_uklad_symetryczny_dodatnio_okreslony(alfa2)
        # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
        test2 = iteracjaprosta.IteracjaProsta(ukl = u2)
        # wyznaczam macierz D i wektor C
        test2.przygotuj()
        # wykonuje iteracje używając metody iteruj_twierdzenie
        iter2 = test2.iteruj_twierdzenie(
            eps = 1e-10,
            norma = self.norma,
            wyswietlaj = 0)
        seria2 = test2.normy.copy()
        niedokl2 = test2.sprawdz_rozwiazanie(self.norma)


                    ### test dla alpha = 0.9
        alfa3 = 0.9
        # okreslam uklad rownan
        u3 = uklad.Uklad(wymiar = self.n)
        # losujemy uklad
        u3.losuj_uklad_symetryczny_dodatnio_okreslony(alfa3)
        # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
        test3 = iteracjaprosta.IteracjaProsta(ukl = u3)
        # wyznaczam macierz D i wektor C
        test3.przygotuj()
        # wykonuje iteracje używając metody iteruj_twierdzenie
        iter3 = test3.iteruj_twierdzenie(
            eps = 1e-10,
            norma = self.norma,
            wyswietlaj = 0)
        seria3 = test3.normy.copy()
        niedokl3 = test3.sprawdz_rozwiazanie(self.norma)

        print(f"Liczba iteracji dla alfa równej {alfa1}: {iter1}")
        print(f"Niedokladnosc rozwiazania: {niedokl1}")
        u1.wypisz_normy_macierzy(macierz = test1.D)
        print(f"\nLiczba iteracji dla alfa równej {alfa2}: {iter2}")
        print(f"Niedokladnosc rozwiazania: {niedokl2}")
        u2.wypisz_normy_macierzy(macierz = test2.D)
        print(f"\nLiczba iteracji dla alfa równej {alfa3}: {iter3}")
        print(f"Niedokladnosc rozwiazania: {niedokl3}")
        u3.wypisz_normy_macierzy(macierz = test3.D)
        wykres_test = wykresy.Wykresy(3)
        wykres_test.badaj_zbieznosc(
            tytul = "Zbieznosc w zależności od parametry alfa",
            opis_OY = "Normy przyblizen",
            dane1 = seria1,
            opis1 = "alfa = 0.1",
            dane2 = seria2,
            opis2 = "alfa = 0.5",
            dane3 = seria3,
            opis3 = "alfa = 0.9"
        )
        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracji prostej"""
        # ustalam zbior parametrow
        # zmieniam je w równych odstępach
        param = [0.1, 0.1615, 0.223, 0.2845, 0.346, 0.4075, 0.469, 0.5305, 0.592, 0.6535, 0.715, 0.7765, 0.838, 0.9]
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar = self.n)
        # dla kazdej wartosci parametru przeprowadzam po k testow
        # i wyswietlam wartosci wybranych charakterystyk eksperymentu
        sr_liczba_iteracji = []
        sr_norma_macierzy = []
        sr_niedokladnosc = []
        for alfa in param:
            norma_macierzy = 0.0
            liczba_iteracji = 0.0
            niedokladnosc = 0.0
            iteracje = 0
            while iteracje < self.k:
                # losujemy uklad
                u1.losuj_uklad_symetryczny_dodatnio_okreslony(alfa)
                # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
                test1 = iteracjaprosta.IteracjaProsta(ukl = u1)
                # wyznaczam macierz D i wektor C
                test1.przygotuj()
                # obliczam norma macierzy D
                norma_D = u1.norma_macierzy(
                        typ = self.norma,
                        macierz = test1.D
                    )
                # wykonuje iteracje używając metody iteruj_twierdzenie
                iter = test1.iteruj_twierdzenie(
                    eps = self.epsilon,
                    norma = self.norma,
                    wyswietlaj = 0)
                niedokl = test1.sprawdz_rozwiazanie(norma = self.norma)
                if iter == 0:
                    # jezeli nie mozna bylo wykonac iteracji
                    # nalezy powtorzyc pomiar
                    continue
                else:
                    # jezeli eksperyment udalo sie przeprowadzic
                    # agregujemy charakterystyki
                    norma_macierzy += norma_D
                    niedokladnosc += niedokl
                    liczba_iteracji += iter
                    iteracje += 1
            # obliczam srednie wartosci charakterystyk
            sr_norma_macierzy.append(norma_macierzy/self.k)
            sr_liczba_iteracji.append(liczba_iteracji/self.k)
            sr_niedokladnosc.append(niedokladnosc/self.k)
        # wypisujemy srednie charakterystyki
        print("Alfa\t||D||\t\tIteracje\tNiedkoladnosc")
        print("------"*9)
        for i in range(len(param)):
            wyniki = f"{param[i]} \t"
            wyniki += f"{sr_norma_macierzy[i]:.6f} \t"
            wyniki += f"{sr_liczba_iteracji[i]:.2f} \t\t"
            wyniki += f"{sr_niedokladnosc[i]:.6e} \n"
            print(wyniki)
        # wykres pokazujący zależność między liczbą iteracji oraz parametrem alfa
        
        plt.figure(facecolor = "white")
        plt.plot(param, sr_liczba_iteracji, "ro")
        plt.title("Zależność liczby iteracji od parametru Alfa")
        plt.xlabel("Alfa")
        plt.ylabel("Liczba iteracji")
        plt.margins(0.1)
        plt.grid(True)
        plt.show()
    
z1 = Zadanie1()
z1.testy()
z1.badaj_zbieznosc()