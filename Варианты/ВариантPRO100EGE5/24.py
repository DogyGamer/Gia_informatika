line = open("./24_12931.txt", "r").readlines()[0].replace("\n", "")
line = line.replace("T", " ").replace("U", " ")
line = line.replace("VWXYZ", "5").replace("WXYZ", "4").replace("XYZ", "3").replace("YZ", "2").replace("Z", "1")

print([x for x in line.split() if len(x) > 5])
