arr = list(map(int, open("C:\\Users\\Admin\\Documents\\Школа\\ЕГЭ\\Информатика\\17\\17_2.txt", "r").readlines()))
max_ends_19 = max([x for x in arr if x % 100 == 19])

cntr = 0
max_val = 0

for i in range(0, len(arr)-2):
    if not any([arr[i] % 3 == 0, arr[i+1] % 3 == 0, arr[i+2] % 3 == 0]):
        continue
    if not sum([arr[i], arr[i+1], arr[i+2]]) > max_ends_19:
        continue
    if not sum([len(str(arr[i])) == 4,len(str(arr[i+1])) == 4, len(str(arr[i+2])) == 4]) == 2:
        continue
    print(arr[i], arr[i+1], arr[i+2])
    cntr += 1
    max_val = max(max_val, sum([arr[i], arr[i+1], arr[i+2]]))
# print(arr)
print(cntr)
print(max_val)