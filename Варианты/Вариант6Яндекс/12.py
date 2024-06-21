def F(s):
    while "2222" in s or "7777" in s:
        if "2222" in s:
            s = s.replace("2222", "77", 1)
        else:
            s = s.replace("7777", "22", 1)
            
    return s

print(F("7"*47))