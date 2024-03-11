inp = open("./26/Homework1/26_3.txt", "r").readlines()

N, S = list(map(int, inp[0].replace("\n", "").split()))

lines = list(map(lambda x: int(x.replace("\n", "")),inp[1:]))

two_hundreds = [x for x in lines if x >= 200 and x <= 210]
others =  sorted([x for x in lines if not (x >= 200 and x <= 210)])

ost = S - sum(two_hundreds)

last_ind = 0
for i in range(1, len(others)):
    if(ost-sum(others[:i+1]) < 0):
        last_ind = i-1
        break

already_gathered = others[:last_ind]
ostalos = others[last_ind:]

ostal = [x for x in ostalos if (ost - sum(already_gathered)) - x > 0 ]


print(others, ost, sum(already_gathered)+max(ostal), len(already_gathered)+1)