# (№ 6784) (Е. Джобс) Текстовый файл 24-274.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита.
# Определите максимальную длину подпоследовательности, которая состоит только из пар символов PC, только из четверок символов CSGO, или из непересекающихся пар символов PC и четверок символов CSGO. 
# Например, в строке ASDPCCSGOPCNGCHPCPCSGOPC есть три подходящие подпоследовательности: PCCSGOPC, РСРС и CSGOPC. Максимальная длина подходящей подпоследовательности – 8. 

# line = open("./24/H1/8.txt", "r").readlines()[0]
# Там нет файла нужного
line = "ASDPCCSGOPCNGCHPCPCSGOPC"


line = line.replace("PC", "?").replace("CSGO", "@")

line = "".join([" " if x != "@" and x != "?" else x for x in line])
maxlen = 0
for sp in line.split():
    leng = sp.count("?")*2 + sp.count("@")*4
    maxlen = max(maxlen, leng)
    
print(maxlen)