import os
from threading import Thread
path = os.path.dirname(os.path.abspath(__file__))+'\\'

gen = 1

num_of_test = 50

def gen_test(dir):
    os.system(f"python {path}{dir}\\manager.py {gen} {num_of_test}")

def gen_problem(num : int):
    if os.path.exists(f"{path}{num}"):
        gen_test(str(num))
        
def gen_all():
    for root,dirs,files in os.walk("./"):
        if root == "./":
            threads : list[Thread] = []
            for dir in dirs:
                if dir == ".vscode" or dir == ".git": continue
                threads.append(Thread(target=gen_test, args=[dir]))
            for t in threads:
                t.start()
            
            for t in threads:
                t.join(20)

gen_problem(213)