stri = open("C:\\Users\\Admin\\Documents\\Школа\\ЕГЭ\\Информатика\\24\\24_3.txt", "r").readlines()[0]
stri = stri.replace("A", "0")
stri = stri.replace("B", "0")
stri = stri.replace("C", "0")
stri = stri.replace("00", "0 0")

print(max([len(x) for x in stri.split()]))


# WRONG CORRECT 49