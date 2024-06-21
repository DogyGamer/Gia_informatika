from itertools import product


maxs = 0
cntr = 0

for n1,n2,n3,n4 in product([0,1,2,3,4,5,6,7,8,9], repeat=4):
    n = int(f"4{n1}8{n2}15{n3}16{n4}23")
    if n % 123 == 42:
        cntr += 1
        maxs = max(maxs, n)
        
print(cntr, maxs)