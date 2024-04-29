# (№ 6651) (Е. Джобс) Текстовый файл 24-263.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита. 
# Определите минимальную длину подстроки, в которой ровно три тройки BAD или FAT. 
# Например, в строке SDFATFDBADZZSFATBADGHTBAD есть три подходящие подстроки FATFDBADZZSFAT, BADZZSFATBAD и FATBADGHTBAD. Минимальная длина 12. 

line = open("./24/H1/24-263.txt", "r").readlines()[0]

line = line.replace("FAT", "@").replace("BAD", "?")

indecies = [i for i in range(len(line)) if line[i] == "?" or line[i] =="@"]

start = 0

min_len = 999_999_999_999


for i in range(2, len(indecies)):
    start = indecies[i-2]
    end = indecies[i]+1
    min_len = min(min_len, end-start)    

print(min_len+6)

# letters = {k:[] for k in "@?"}

# for i in range(len(line)):
#     s = line[i]
    
#     if s in letters.keys():
#         letters[s].append(i)
#         if sum([len(x) for x in letters.values()]) > 3:
#             start = letters[s].pop() + 1
            
#         for s2 in letters.keys():
#             letters[s2] = [x for x in letters[s2] if x >= start]
            
#         if sum([len(x) for x in letters.values()]) == 3:
#             min_len = min(min_len, (i-start) + (6))
            
# print(min_len)