import random
import time
from numba import jit

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

class Finde:
    def __init__(self):
        self.i = 0
        self.n = 0

    def random_numbers(self, nn):
        (self.i, self.n) = self.random_numbers_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def random_numbers_static(nn):
        i = 0
        n = 0
        for _ in range(nn):
            sumofR = 0
            i += 1
            while sumofR < 1:
                r = random.random()
                sumofR += r
                n += 1
                if sumofR >= 1:
                    break
        return i, n


    def value_of_e(self):
        return self.n / self.i