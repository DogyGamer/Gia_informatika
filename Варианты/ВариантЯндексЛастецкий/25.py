from math import floor

cntr = 0

for i in range(625681, 758641):
    dels = []
    if floor(i**0.5)**2 == i:
        for d in range(2, floor(i**0.5)-1):
            if i % d == 0:
                if d < 10:
                    dels =[]
                    break
                else:
                    dels.append(d)
    if len(dels) == 3:
        print(i // dels[1], i // dels[0])

# 10309 48373
# 13583 37553
# 8833 58619
# 15523 35131
# 19573 31487
# 9559 68651