import random
import time


class Tictoc:
    def __init__(self):
        self.t1= 0
        self.t2=0

    def tic(self):
        self.t1 =time.time()

    def toc(self):
       self.t2 = time.time()
       return self.t2 - self.t1


class Finde:
    def __init__(self):
        self.i = 0
        self.n = 0

    def random_numbers(self, nn):
        for _ in range(nn):
            sumofR = 0
            self.i += 1
            while sumofR < 1:
                r = random.random()
                sumofR += r
                self.n += 1
                if sumofR >= 1:
                    break
    def value_of_e(self):
        return self.n / self.i