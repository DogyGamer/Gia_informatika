strings = open("./26/Homework1/26_1.txt", "r").readlines()
S, N = list(map(int, strings[0].replace("\n", "").split()))

def prep(x):
    return int(x.replace("\n", ""))

arr = sorted(list(map(prep, strings[1:])))


last_ind = 0
for i in range(1, len(arr)):
    if(S-sum(arr[:i+1]) < 0):
        last_ind = i-1
        break
    
# print(last_ind)
print(len(arr[:last_ind+1]))
# print(S-sum(arr[:last_ind+1]))
# print(arr[:last_ind+1][-1]+S-sum(arr[:last_ind+1]))
print(max([x for x in set(arr) if x > arr[:last_ind+1][-1] and x <= arr[:last_ind+1][-1]+S-sum(arr[:last_ind+1])]))