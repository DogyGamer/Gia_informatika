file = open("17_1.txt", "r")
chet_array = []
def filt(x):
    x = int(x)
    if(x % 2 == 0):
        chet_array.append(x)
    return x
array = list(map(filt,file.readlines()))

average = sum(chet_array) / len(chet_array)
res = []
res_sums = []
for i in range(len(array)-1):
    if ((array[i] % 3 == 0) or (array[i+1] % 3 == 0)) and ((array[i+1] < average) or (array[i] < average)):
        res.append((array[i], array[i+1]))
        res_sums.append(array[i]+array[i+1])

print(len(res), max(res_sums))

