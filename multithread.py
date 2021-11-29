from main import Tictoc, Finde
import os
from threading import Thread

if __name__ == "__main__":
    tt = Tictoc()
    tt.tic()
    b = 100000
    find_es = []
    threads = []
    for i in range(os.cpu_count()):
        find_es.append(Finde())
        threads.append(Thread(target=find_es[i].random_numbers, args=(b,)))
        print("Started thread number #%d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    inner = 0
    total = 0
    for find_e in find_es:
        inner += find_e.n
        total += find_e.i
    print("E = %.8f | TIME = %.6f seconds" % (inner/total,tt.toc()))