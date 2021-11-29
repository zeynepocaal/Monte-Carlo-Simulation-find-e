from main import Tictoc , Finde

if __name__ == "__main__":
        tt = Tictoc()
        tt.tic()
        finding_e = Finde()
        finding_e.random_numbers(1000000)
        e = finding_e.value_of_e()
print("E =  %.8f" % e)
print("TIME = %.6f seconds" % (tt.toc()))
