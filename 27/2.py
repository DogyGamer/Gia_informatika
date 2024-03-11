lines = open("./27/2-B.txt", "r").readlines()[1:]

S = 0
mindiv = 999_999_999

for line in range(len(lines)):
    a, b = list(map(int, lines[line].split()))
    
    S+= max(a,b)
    if a % 3 != b % 3:
        mindiv = min(mindiv, max(a,b)-min(a,b))
    
if S % 3 == 0:
    S -= mindiv

print(S)
