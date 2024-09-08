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
    len_range = (5, 100)
    char_set = ["R", "I", "N", "G", "S"]

    def randc():
        return random.choice(char_set)

    if test_num <= 5:
        n = 5
        ins_len = random.randint(2, 3)
        ins = ""
        hell = ""
        hev = ""
        for _ in range(ins_len):
            ins += randc()
        for _ in range(n):
            hell += randc()
            hev += randc()
        print(ins, file=inp_file)
        print(hell, file=inp_file)
        print(hev, file=inp_file)
    else:
        n = 0
        ins_len = 0  # must less than n
        ins = ""
        hell = ""
        hev = ""

        if test_num <= 15:
            n = 100
            ins_len = random.randint(5, 100)
            for _ in range(ins_len):
                ins += randc()
            j = 0
            for i in range(n):
                chance = ins_len / 100
                took = 0
                if random.random() <= chance and i < ins_len:
                    hell += ins[i]
                    i += 1
                    took = 1
                else:
                    hell += randc()
                if random.random() <= chance and not took and i < ins_len:
                    hev += ins[i]
                    i += 1
                else:
                    hev += randc()
        elif test_num <= 20:
            n = 100
            ins_len = random.randint(5, 100)
            for _ in range(ins_len):
                ins += randc()

            for _ in range(n):
                char = randc()
                hell += char
                hev += char
        elif test_num <= 25:
            n = 100
            ins_len = random.randint(5, 100)
            exclude = []
            num_ex = random.randint(1, 2)
            for _ in range(num_ex):
                exclude.append(randc())
            for _ in range(n):
                c = randc()
                while c in exclude:
                    c = randc()
                hell += c
            for _ in range(n):
                c = randc()
                while c in exclude:
                    c = randc()
                hev += c
        elif test_num <= 26:
            n = 100
            for _ in range(n):
                hell += randc()
            ins = hell
            hev = "R" * n
        elif test_num <= 27:
            n = 100
            hell = "R" * n
            hev = "S" * n
            ins = "G" * n
        elif test_num <= 28:
            ins = "RGS"
            hell = "RRS"
            hev = "GRR"
        elif test_num <= 35:
            n = 100
            ins_len = random.randint(5, 100)
            for _ in range(ins_len):
                ins += randc()
            for i in range(n):
                hell += randc()
                c = randc()
                while c == hell[i]:
                    c = randc()
                hev += c
        else:
            n = 100
            ins_len = random.randint(5, 100)
            for _ in range(ins_len):
                ins += randc()
            j = 0
            for i in range(n):
                chance = ins_len / 100
                took = 0
                if random.random() <= chance and i < ins_len:
                    hell += ins[i]
                    i += 1
                    took = 1
                else:
                    hell += randc()
                if random.random() <= chance and not took and i < ins_len:
                    hev += ins[i]
                    i += 1
                else:
                    hev += randc()
            c = randc()
            while c == ins[ins_len - 1]:
                c = randc()
            hell.replace(ins[ins_len - 1], c)
            c = randc()
            while c == ins[ins_len - 1]:
                c = randc()
            hev.replace(ins[ins_len - 1], c)
            chance = 0.5
            if random.random() <= chance:
                hell = hell[: n - 1] + ins[ins_len - 1]
                if random.random() <= chance:
                    hev = hev[: n - 1] + ins[ins_len - 1]
            else:
                hev = hev[: n - 1] + ins[ins_len - 1]
                if random.random() <= chance:
                    hell = hell[: n - 1] + ins[ins_len - 1]

        """
        max inp/

        top and bottom =/

        some char dont appear in instruct/

        cant move/

        top & bot completely diff/

        top row is valid but not bottom

        last move is at the end
        """
        print(ins, file=inp_file)
        print(hell, file=inp_file)
        print(hev, file=inp_file)

with open(inp_dir, "r") as inp_file, open(out_dir, "w") as output:
    process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
    process.communicate()
