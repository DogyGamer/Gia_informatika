lines = list(map(int, open("./26(3).txt", "r").readlines()[1:]))
lines = sorted(lines)

l_ch = [l for l in lines if l % 2 == 0]
l_nch = [l for l in lines if l % 2 != 0]

print(l_ch)
print(l_nch)

min_mass = 0

grabbed_gir_ch = []
grabbed_gir_nch = []

ptr1 = 0
ptr2 = 0

while True:
    min_mass += 1