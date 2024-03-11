# +1 +4 *2
# >= 47

moves_left = [0]*97

def get_win_moves(N):
    res = []
    if(moves_left[N * 2] % 2 == 0):
        res.append(moves_left[N*2])
    if(moves_left[N+4] % 2 == 0):
        res.append(moves_left[N+4])
    if(moves_left[N+1] % 2 == 0):
        res.append(moves_left[N+1])
        
    return res

for i in range(46, 0, -1):
    wmv = get_win_moves(i)
    
    if len(wmv) == 0:
        moves_left[i] = max(moves_left[i*2], moves_left[i+4], moves_left[i+1]) + 1
        pass
    else:
        moves_left[i] = min(wmv)+1
        
    

for i in range(1, len(moves_left)):
    print(i, "\t", moves_left[i])