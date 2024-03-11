import math


pow_of_two = [2**x for x in range(0, 50, 2)]
pow_of_three = [3**x for x in range(1,50,2)]


res = []
for twos in pow_of_two:
    for threes in pow_of_three:
        N = twos*threes
        if  N >= 200000000 and N <= 400000000:
            res.append(N)
res.sort()
print(res)
