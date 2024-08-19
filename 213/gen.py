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
#FIXME!!!: test.out is empty
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

            2 broken next to each other = 0

            last stair is broke = 0

            this situation :  ..xoxoox..

            normal possible case
            
        '''
        n,k = 1,0
        d = {}
        chance = random.randint(1,5)

        def possible(pos):
            return d.get(pos-1) == None and d.get(pos+1) == None and d.get(pos) == None

        match chance:
            case 1:
                n = 100000
            case 2:
                n,k = 100000, 10
                while len(d) < k:
                    num = random.randint(2,n-1)
                    if possible(num) and len(d) < k-1:
                        d[num] = 1
                    elif len(d) == k-1:
                        for k in d.keys():
                            if d.get(k+1) == None:
                                d[k+1] = 1
                                break

            case 3:
                n = 100000
                k = 10
                while len(d) < k-1:
                    num = random.randint(2,n-2)
                    if possible(num):
                        d[num] = 1
                d[n]=1
            case 4:
                n = 100000
                k = 10
                pos = random.randint(2,n-10)
                d[pos] = 1
                d[pos+2] = 1
                d[pos+5] = 1

                while len(d) < k-3:
                    num = random.randint(2,n-2)
                    if possible(num) and (num < pos or num > pos + 5):
                        d[num] = 1
            case _:
                n = 100000
                k = 10

                while len(d) < k:
                    num = random.randint(2,n-1)
                    if possible(num):
                        d[num] = 1        

        print(n,k,file=inp_file)
        print(("{} "*(len(d))).format(*[k for k in d.keys()]), file=inp_file)
    #stop gen test here
print(f"generate {test_num} doesnt stuck")
with open(inp_dir,"r") as inp_file, open(out_dir, "w") as output:  
    process = subprocess.Popen(f"{path}sol.exe", stdin=inp_file, stdout=output)
    process.communicate()

