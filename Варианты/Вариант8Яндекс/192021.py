moves = [0]*(80*3)

def gwmvs(i):
    steps = [i+3, i*2, i*3]
    mvs = [moves[x] for x in steps]
    return mvs, [mvs[i] for i in range(3) if mvs[i] % 2 == 0 and steps[i] <= 77]

for i in range(54, 0, -1):
    mvs, wmvs = gwmvs(i)
    if len(wmvs) == 0:
        moves[i] = max(mvs) + 1
    else:
        moves[i] = min(wmvs) + 1

for i in range(1, 54):
    r = moves[i]
    if r == 4:
        print(i, r)