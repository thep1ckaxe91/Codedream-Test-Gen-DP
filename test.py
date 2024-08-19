s = ""

l = []
with open("log.txt","r") as log:
    for line in log.readlines():
        try:
            n = int(line)
            l.append(n)
        except:
            continue

for i in range(1,51):
    if not i in l:
        print(i)