lines = open("./26/Homework1/26_6.txt", "r").readlines()
S, N = map(int, lines[0].split())
lines = list(map(int, lines[1:]))
lines.sort()

last_ind = 0
for i in range(len(lines)):
    if S - sum(lines[:i]) < 0:
        last_ind = i - 1
        break

ost = S - sum(lines[:last_ind-1])

max_val = 0
for i in range(last_ind-1, len(lines)):
    if ost - lines[i] >= 0:
        max_val = max(max_val, lines[i]) 

print(len(lines[:last_ind]), max_val)
# 1612 65 ANS
# 1612 90 Correct

# 1612 90 Corrected