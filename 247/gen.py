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
    if test_num <= 5:
        T = random.randint(3, 20)
        n, m = random.randint(5, 10), random.randint(5, 10)
        small = []
        big = []
        start = random.randint(1, 5)
        for i in range(n):
            small.append(start)
            start += random.randint(1, 3)
        start = random.randint(1, 5)
        for i in range(m):
            big.append(start)
            start += random.randint(1, 3)
        print(T, file=inp_file)
        print(n, file=inp_file)
        for x in small:
            print(x, file=inp_file, end=" ")
        print("", file=inp_file)
        print(m, file=inp_file)
        for x in big:
            print(x, file=inp_file, end=" ")

    else:
        t = 0
        n, m = 0, 0
        small = []
        big = []
        """
        Cases:
            t=m=n=1

            max case

            every pack =

            t=1000 sum(small,big)=999/1001

            all package near t


        """

        if test_num <= 7:
            t = 1
            n = 1
            m = 1
            small.append(1 + (test_num == 7))
            big.append(1)
        elif test_num <= 20:
            t = 1000
            n = 1000
            m = 1000
            for i in range(n):
                small.append(random.randint(1, 1000))
            for i in range(m):
                big.append(random.randint(1, 1000))
        elif test_num <= 30:
            t = random.randint(10, 500)
            n = random.randint(10, 1000)
            m = random.randint(10, 1000)

            val = random.randint(1,t)

            small = [val for _ in range(n)]
            big = [val for _ in range(m)]
        elif test_num <= 40:
            t = 1000
            while sum(small) + sum(big) < 2 * t:
                chance = 0.7
                if random.random() < chance:
                    small.append(random.randint(50,300))
                else:
                    big.append(random.randint(50,300))
            n = len(small)
            m = len(big)
        else:
            t = 1000
            n = 1000
            m = 1000
            for _ in range(1000):
                small.append(random.randint(1,1000))
                big.append(random.randint(1,1000))
                
        print(t, file=inp_file)
        print(n, file=inp_file)
        small.sort()
        big.sort()
        for x in small:
            print(x, file=inp_file, end=" ")
        print("", file=inp_file)
        print(m, file=inp_file)
        for x in big:
            print(x, file=inp_file, end=" ")

with open(inp_dir, "r") as inp_file, open(out_dir, "w") as output:
    process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
    process.communicate()
