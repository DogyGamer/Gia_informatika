n,k,d = list(map(int, input().split()))
n_2 = n*10
ost = n_2 % k
if ost != 0:
    new_digit = k - (n_2 % k)
else:
    new_digit = 0
if new_digit > 9:
    print(-1)
    exit(0)
n = str(n)+str(new_digit)+"0"*(d-1)
print(n)