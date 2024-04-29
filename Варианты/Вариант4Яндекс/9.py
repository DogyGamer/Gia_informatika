lines = open("./9(2).csv", "r").readlines()

matrix = [list(map(int, lines[i].replace("\n", "").split(";"))) for i in range(len(lines))]

# print(matrix)

# matrix = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
# ]

def getsosedy(x,y):
    sosedi = []
    
    if x != 0:
        sosedi.append(matrix[x-1][y])
        if y != len(matrix[0])-1:
            sosedi.append(matrix[x-1][y+1])
        if y != 0:
            sosedi.append(matrix[x-1][y-1])
    
    if x != len(matrix)-1:
        sosedi.append(matrix[x+1][y])
        if y != len(matrix[0])-1:
            sosedi.append(matrix[x+1][y+1])
        if y != 0:
            sosedi.append(matrix[x+1][y-1])
        
    if y != len(matrix[0])-1:
        sosedi.append(matrix[x][y+1])
    if y != 0:
        sosedi.append(matrix[x][y-1])
    
    return sosedi


sm = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        a = matrix[x][y]
        sosedi = getsosedy(x,y)
        
        if any([a == sosed for sosed in sosedi]) and all([a >= sosed for sosed in sosedi]):
            sm += a
print(sm)