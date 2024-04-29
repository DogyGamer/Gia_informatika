from itertools import product

acntr = 0

for a in product("0123456789ABCDEF", repeat=5):
    if a[0] == "0":
        continue
    
    cntr = 0
    for b in a:
        if b in "0123456789":
            cntr += 1
            
    if cntr == 1:
        acntr += 1
        
print(acntr)