import os
from threading import Thread
path = os.path.dirname(os.path.abspath(__file__))+'\\'

gen = 1

num_of_test = 100

def gen_test(dir):
    os.system(f"python {path}{dir}\\manager.py {gen} {num_of_test}")


for root,dirs,files in os.walk("./"):
    if root == "./":
        threads : list[Thread] = []
        for dir in dirs:
            if dir == ".vscode": continue
            threads.append(Thread(target=gen_test, args=[dir]))
        for t in threads:
            t.start()
        
        for t in threads:
            t.join()