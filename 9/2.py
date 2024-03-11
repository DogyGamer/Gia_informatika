strings = open("./9/2.csv", "r").readlines()

counter = 0

for s in strings:
    string = s.split("\n")[0].replace("п»ї", "").split(";")
    sss = list(map(int, string))

    if (len(set(sss)) != len(sss)):
        continue

    ch_c = 0
    ch_s = 0

    nch_c = 0
    nch_s = 0
    for x in sss:
        if(x % 2 == 0):
            ch_c +=1
            ch_s += x
        else:
            nch_c +=1
            nch_s +=x
    # chetnechet = [x % 2 == 0 for x in sss]

    if(ch_c <= nch_c):
        continue

    if(ch_s >= nch_s):
        continue

    counter += 1

print(counter)