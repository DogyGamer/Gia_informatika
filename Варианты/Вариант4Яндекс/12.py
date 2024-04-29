
def f(stri):
    while "44" in stri or "9299" in stri or "49" in stri:
        stri = stri.replace("49", "944", 1)
        stri = stri.replace("44", "2", 1)
        stri = stri.replace("9299", "4", 1)
        
    return stri

ans = []

for n in range(3, 1000):
    stri = "4"+"9"*n
    ans.append(f(stri))
    
print(len(set(ans)))