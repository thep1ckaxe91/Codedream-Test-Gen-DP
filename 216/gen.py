import subprocess
import sys
import os
import random

path = os.path.dirname(os.path.abspath(__file__)) + "\\"

if sys.argv[2] == "nogen":
    exit()

test_num = int(sys.argv[1])
test_dir = f"{path}TEST\\TEST{test_num:03d}"
os.makedirs(test_dir, exist_ok=True)

inp_dir = test_dir + f"\\test.inp"
out_dir = test_dir + f"\\test.out"

with open(inp_dir, "w") as inp_file:
    # gen test here
    if test_num <= 5:
        n = random.randint(10, 15)
        val_range = (0, 50)
        print(n, file=inp_file)
        for i in range(n):
            a, b, c = (
                random.randint(*val_range),
                random.randint(*val_range),
                random.randint(*val_range),
            )
            print(a,b,c,file=inp_file)
        
    else:
        n = random.randint(1000, 100000)
        if test_num == 50:
            n = 100000
        elif test_num == 20:
            n = 1
        elif test_num == 10:
            n = 10000
        val_range = (0, 1000)
        print(n, file=inp_file)
        for i in range(n):
            a, b, c = (
                random.randint(*val_range),
                random.randint(*val_range),
                random.randint(*val_range),
            )
            print(a,b,c,file=inp_file)
import threading
lock = threading.Lock()
with lock:
    with open(inp_dir, "r") as inp_file, open(out_dir, "w") as output:
        process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
        process.communicate()
        