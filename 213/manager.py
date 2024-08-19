import os
import sys
from threading import Thread
path = os.path.dirname(os.path.abspath(__file__))+'\\'

os.system(f"g++ {path}sol.cpp -o {path}sol.exe")

 
gen = "nogen"
if sys.argv[1] == "1":
    gen = "gen"

num_of_test = int(sys.argv[2])

def gen_test(i):
    os.system(f"python {path}gen.py {i} {gen}")
threads : list[Thread] = []
#gen small test case
for i in range(1,num_of_test+1):
    gen_test(i)
#     threads.append(Thread(target=gen_test,args=[i]))
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
    
