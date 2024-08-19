s = "generate 13 doesnt stuck""generate 10 doesnt stuck""generate 8 doesnt stuck""generate 4 doesnt stuck""generate 11 doesnt stuckgenerate 20 doesnt stuck""generate 2 doesnt stuck""generate 27 doest stuck""generate 3 doesnt stuck""generate 15 doesnt stuck""generate 23 doesnt stuckgenerate 14 doesnt stuckgenerate 17 doesnt stuck""generate 16 doesnt stuckgenerate 28 doesnt stuckgenerate 36 doesnt stuckgenerate 35 doesnt stuck""generate 40 doesnt stuckgenerate 7 doesnt stuck""generate 43 doesnt stuck""generate 5 doesnt stuckgenerate 32 doesnt stuck""generate 45 doesnt stuck""generate 30 doesnt stuck""generate 37 doesnt stuck""generate 31 doesnt stuck""generate 44 doesnt stuck""generate 46 doesnt stuck""generate 49 doesnt stuck""generate 21 doesnt stuck""generate 50 doesnt stuckgenerate 42 doesnt stuck""generate 33 doesnt stuck""generate 41 doesnt stuck""generate 29 doesnt stuck""generate 19 doesnt stuck""generate 39 doesnt stuck"

ss = s.split()
l = []
for s in ss:
    try:
        n = int(s)
        l.append(n)
    except:
        pass

l.sort()
print(l)