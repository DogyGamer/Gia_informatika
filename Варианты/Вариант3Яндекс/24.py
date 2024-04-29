line = open("./Вариант3Яндекс/24.txt", "r").readlines()[0]

line2 = line.replace("ABA", "@")
line2 = line2.replace("BAB", "?")

line3 = line.replace("BAB", "?") 
line3 = line3.replace("ABA", "@")

line4 = line3.replace("A", " ").replace("B", " ").replace("C", " ").split()
line5 = line2.replace("A", " ").replace("B", " ").replace("C", " ").split()

len1 = max([len(x) for x in line4])
len2 = max([len(x) for x in line5])
print(len1, len2)
