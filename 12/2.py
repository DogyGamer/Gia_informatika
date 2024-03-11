string = '9'*127

while '333' in string or '999' in string:
    if '333' in string:
        print(1)
        string = string.replace('333', '9', 1)
    elif '999' in string:
        print(2)
        string = string.replace('999', '3', 1)
    else:
        print(3)
        break
print(string)
    