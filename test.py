s = ""

with open("log.txt","r") as log:
    s = log.read()
ss = s.split()
l = []
for s in ss:
    try:
        n = int(s)
        l.append(n)
    except:
        pass

for i in range(1,51):
    if not i in l:
        print(i)