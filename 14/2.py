
def calc_val(arr):
    res = 0
    for n in range(len(arr)):
        res += arr[n] * (158**n)

    return res

ans = []
for x in range(0,158):
    val1 = calc_val([2,x,3,7,2])
    val2 = calc_val([0,9,3,x,1])
    value = val1 + val2
    if(value % 73 == 0):
        ans.append(value / 73)


print(ans)
print("\n")
print(sum(ans))
# 10 in 158
print(calc_val([0,1]))