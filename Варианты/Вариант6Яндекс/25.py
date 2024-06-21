import fnmatch

n = 1
n2 = 1

while 2024 * n < 10**10:
    a = 2024 * n
    if fnmatch.fnmatch(str(a), "10*2024?"):
        print(n2, a, n)
        n2 += 1
    
    n += 1