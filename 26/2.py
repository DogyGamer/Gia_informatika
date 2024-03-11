text = open(".\\26\\26_2.txt", "r").readlines()[1:]
def prep(el):
    return list(map(int, el.split()))

text = list(map(prep, text))

array = sorted(text, key=lambda x: x[1])

ans = [0]

prime_st, prime_ed = array[0]



for i in range(1, len(array)):
    start, end = array[i]
    
    if not (start - prime_ed >= 15):
        continue
    
    ans.append(i)
    prime_st, prime_ed = start, end
    
    
print(len(ans), array[ans[-1]][0] - array[ans[-2]][1], )

# start  end
