import itertools
a = itertools.product([0,1,2,3,4,5,6,7], repeat=11)
c = 0

for n in a:
    nechet_c = 0
    nechet_c += n.count(1)
    nechet_c += n.count(3)
    nechet_c += n.count(5)
    nechet_c += n.count(7)
    if(nechet_c != 3):
        continue
    
    prev_symb = False

    flag = True
    for symb in n:
        if symb % 2 != 0:
            n_symb = True
        else:
            n_symb = False

        if(prev_symb and n_symb):
            flag = False
            break

    if(flag):
        c+=1