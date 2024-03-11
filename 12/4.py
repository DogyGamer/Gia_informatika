stri = "2"+"9"*100
print(stri)
while True:
    if("19" in stri):
        stri = stri.replace("19", "2", 1)
    elif("299" in stri):
        stri = stri.replace("299", "3", 1)
    elif ("3999" in stri):
        stri = stri.replace("3999", "1",1)
    else:
        break
    
    print(stri)
    
print(stri)