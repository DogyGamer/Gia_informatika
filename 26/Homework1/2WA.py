from math import ceil

lines = list(map(lambda x: int(x.replace("\n", "")), open("./26/Homework1/26_2.txt", "r").readlines()[1:]))

lines.sort(reverse=False)

lower_50 = [x for x in lines if x <= 50]
upper_50 = [x for x in lines if x > 50]

i = 0
j = len(upper_50)-1

high_sum = 0
low_sum = 0

low_max = 0

while i != j and i < j:
    i+= 1
    j = len(upper_50)-1-i
    if (i == j or i > j):
        break
    low_sum += ceil(upper_50[i] * 0.75)
    high_sum += upper_50[j]   
    low_max = max(low_max, upper_50[i]) 


print(sum(lower_50) + low_sum + high_sum, low_max)
# 469784 511
# 469827 512
# 468932 511