stroka = open("24_1.txt", "r").readlines()[0]
lens = map(len, stroka.split("XZZY"))
print(max(lens)+6)
