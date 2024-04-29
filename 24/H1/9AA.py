# (№ 6782) (ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита и цифры.
# Определите максимальную длину подстроки, в которой ни одна буква не стоит рядом с буквой и ни одна цифра не стоит рядом с цифрой. 

line = open("./24/H1/9.txt", "r").readlines()[0]

clen = 0
maxlen = 0

prev_was_number = not line[0].isdigit()

start = 0

for i in range(len(line)):
    s = line[i]
    
    if s.isdigit() == prev_was_number:
        start = i
    else:
        maxlen = max(maxlen, i-start+1)
        
    prev_was_number = s.isdigit()
    
print(maxlen)