a = {
    1 : 1,
    2 : 2,
    3 : 3
}

print(("{} "*(len(a))).format(*[k for k in a.keys()]))