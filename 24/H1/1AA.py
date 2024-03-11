line = open("./24/H1/1.txt", "r").readlines()[0].replace("\n", "")

start = 0
letters = {"S": [], "U": [], "N":[]}


max_len = 0

for i in range(1, len(line)):
    symbol = line[i]
    if symbol == "X" or symbol == "Y":
        start = i+1
        continue
    
    if symbol in letters.keys():
        letters[symbol].append(i)
        
        if len(letters[symbol]) > 10:
            start = letters[symbol].pop() + 1
            
            for let in letters.keys():
                letters[let] = [x for x in letters[let] if x > start]

    max_len = max(max_len, i-start+1)
    
    

print(max_len)
    
