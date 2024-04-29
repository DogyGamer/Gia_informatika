# (№ 7196) Текстовый файл 24-280.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита. 
# Определите максимальное количество идущих подряд символов, среди которых буквы X и Y встречаются не более пяти раз. 

line = open("./24/H1/6.txt", "r").readlines()[0].replace("\n", "")

start = 0
maxlen = 0

letters = {k:[] for k in "XY"}

for i in range(1, len(line)):
    s = line[i]
    
    if s in letters.keys():
        letters[s].append(i)
        if len(letters[s]) > 5:
            start = letters[s].pop()
            # for _ in range(len(letters[s]) - 5):
            
        for s2 in letters.keys():
            letters[s2] = [x for x in letters[s2] if x > start]
            
    maxlen = max(maxlen, i-start-1)
print(maxlen)