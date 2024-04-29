

11100000 - 224
10001011
10000000
10011111 - 159

left_bytes_zeros = bin(227)[2:].count("0") + bin(31)[2:].count("0") + 2

max_a = 0
for A in range(0,256):
    zeros_in_a = bin(A)[2:].count("0") + (8-len(bin(A)[2:]))
    arr = [left_bytes_zeros <= zeros_in_a + bin(x)[2:].count("0") for x in range(128, 255)]
    if all(arr):
        max_a = max(max_a, A)
        
print(max_a)

# 240 - ANS

# 13 строка, правильный ответ дало, только когда поставил до 254 вкл. хотя по идее нужное число до 159 вкл