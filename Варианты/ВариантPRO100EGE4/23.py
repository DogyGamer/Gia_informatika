from itertools import product

result = []

for i in range(0,69):
    print(i, 68-i)
    res = 1
    res += 3*i
    res -= 2*(68-i)
    
    result.append(res)
    
print(result, len(result))