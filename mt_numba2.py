from mt_numba import TicToc, Finde



if __name__ == "__main__":
    tt= TicToc()
    tt.tic()
    finding_e = Finde()
    finding_e.random_numbers(100000)
    e = finding_e.value_of_e()
print("E =  %.8f" % e)
print("TIME = %.6f seconds" % (tt.toc()))