string = open("24_2.txt", "r").readlines()[0]

ans = {}

for i in range(1, len(string)-1):
    if(string[i-1] == string[i+1]): 
        if (string[i] in ans):
            ans[string[i]] +=1
        else:
            ans[string[i]] = 1


lmax = 0
letter = ''

for key, value in ans.items():
    if(value > lmax):
        lmax = value
        letter = key
    print(key, value)

print(letter, lmax)
# print(ans)