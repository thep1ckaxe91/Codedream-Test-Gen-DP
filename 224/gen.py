import subprocess
import sys
import os
import random
path = os.path.dirname(os.path.abspath(__file__))+'\\'

if(sys.argv[2] == "nogen"):
    exit()

test_num = int(sys.argv[1])
test_dir = f"{path}TEST\\TEST{test_num:03d}"
os.makedirs(test_dir,exist_ok=True)

inp_dir = test_dir+f"\\test.inp"
out_dir = test_dir+f"\\test.out"

with open(inp_dir,"w") as inp_file:
    if test_num <= 5:
        n,k = random.randint(5,10),random.randint(4,5)
        print(n,k,file=inp_file)
        for i in range(n):
            print(random.randint(1,5),end=" ",file=inp_file)
    else:
        n,k = 1000,random.randint(1,1000)
        print(n,k,file=inp_file)
        for i in range(n):
            print(random.randint(1,100000),end=" ",file=inp_file)

import threading
lock = threading.Lock()
with lock:
    with open(inp_dir, "r") as inp_file, open(out_dir, "w") as output:
        process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
        process.communicate()
