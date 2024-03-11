moves_left = [0]*(30+11)

def get_win_moves(S):
    winmoves = []
    if moves_left[S+1] %2 == 0:
        winmoves.append(moves_left[S+1])
    
    if moves_left[S+10] % 2 == 0:
        winmoves.append(moves_left[S+10])
        
    return winmoves



for i in range(30, 0, -1):
    moves = get_win_moves(i)
    
    if len(moves) == 0:
        moves_left[i] = max(moves_left[i+1], moves_left[i+10]) + 1
    else:
        moves_left[i] = min(moves) + 1
        
for i in range(len(moves_left)):
    print(i, moves_left[i], sep="\t")