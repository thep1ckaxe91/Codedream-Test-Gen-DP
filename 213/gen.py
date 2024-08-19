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
    #gen test here
    if test_num <= 5: #gen readable test
        n,k = random.randint(5,10), random.randint(0,10)
        k = min(n//3,k)
        d = {}
        for _ in range(k):
            num = 0
            while True:
                num = random.randint(2,n)
                if d.get(num) == None:
                    chance = random.random()*100
                    if chance < 95:
                        if d.get(num-1)!=None or d.get(num+1)!=None or num == n:
                            continue
                        else:
                            d[num]=1
                    else:
                        d[num]=1
                    break
                else:
                    continue
        print(n,k,file=inp_file)
        print(("{} "*(len(d))).format(*[k for k in d.keys()]), file=inp_file)
    else: #gen large, strong test
        '''
        cases:
            no broken stair at all

            2 broken next to each other

            last stair is broke

            
        '''


        n,k = 0,0
        d = {}
        chance = random.random()*100
        if chance < 20: 

        print(n,k,file=inp_file)
        print(("{} "*(len(d))).format(*[k for k in d.keys()]), file=inp_file)
    #stop gen test here

with open(inp_dir,"r") as inp_file, open(out_dir, "w") as output:  
    process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
    process.communicate()

