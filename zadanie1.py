"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        eps = 1.0E-6
        norma = 0
        alfa = [0.1, 0.5, 0.9]
        
        for a in alfa:
            u1 = uklad.Uklad(100)
            u1.losuj_uklad_symetryczny_dodatnio_okreslony(a)
            
            i1 = iteracjaprosta.IteracjaProsta(u1)
            i1.przygotuj()
            i1.iteruj_twierdzenie(eps, norma, 1)
        
        
        
        return 0
        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracyjnej"""
        # miejsce na realizacje eksperymentu - drugiej czesci zadania 1

        return 0
    
z1 = Zadanie1()
z1.testy()