line = open("./24(6).txt", "r").readlines()[0].replace("\n", "")

lines = line.split("AHAHA")
arr = [[lines[x], len(lines[x]), x] for x in range(len(lines))]
print(max(arr, key=lambda x: x[1]))

print(lines[8477], lines[8478], lines[8479])