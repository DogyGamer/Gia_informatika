lines = list(map(lambda x: int(x.replace("\n", "")), open("./17_12926.txt", "r").readlines()))

max_2 = max([x for x in lines if len(str(x).replace("-", "")) == 2 ])


cntr = 0
msum = 999_999_999_999

A = 0
for i in range(0, len(lines)-3):
    arr = lines[i:i+4]

    first_last_digit = str(arr[0])[-1]
    if all([str(x)[-1] == first_last_digit for x in arr]):
        A = max(A, sum(arr))
      
  
for i in range(0, len(lines)-4):
    arr = lines[i:i+5]
    if sum(arr) % max_2 != 0:
        continue
    
    if len([x for x in arr if x < A]) == 1:
        cntr += 1
        msum = min(msum, sum(arr))
        

print(cntr, msum)