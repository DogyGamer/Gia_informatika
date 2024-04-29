line = open("./24.txt", "r").readlines()[0].replace("\n", "")

is_last_letter = line[0] in "ABC"
leng = 1

maxleng = 0

for i in range(1, len(line)):
    a = line[i]
    is_a_letter = a in "ABC"
    
    if is_a_letter == is_last_letter:
        maxleng = max(maxleng, leng)
        leng = 1
    else:
        leng += 1
    
    is_last_letter = is_a_letter
    
print(maxleng)