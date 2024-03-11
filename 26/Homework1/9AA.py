lines = list(map(lambda x: list(map(int, x.split())), open("./26/Homework1/26_9.txt", "r").readlines()[1:]))
start_date = 1_633_046_400 
week_start = 1_633_305_600
week_end = week_start + 604800


# Какие отсеиваем
# Начало процесса >= конца периода
# Конец процесс <= начала периода


data = []
for start, end in lines: #Отбрасываем промежутки которые не лежать в искомом пространстве
    if start >= week_end:
        continue
    if end <= week_start:
        if end != 0:
            continue
    
    if start <= week_start or start == 0:
        start = week_start
    
    if end >= week_end or end == 0:
        end = week_end
    
    data.append([start, end])
    
data.sort(key=lambda x: x[0])

data2 = []
for i in range(len(data)):
    start, end = data[i]
    data2.append([start, i, True])
    data2.append([end, i, False])
    
data2.sort(key=lambda x: x[0])
    
print(data2)
    
process_counter = 0
lmax = 0
lmaxind = 0
for dat in data2:
    if dat[2]:
        process_counter += 1
    else:
        process_counter -= 1
        
    if process_counter > lmax:
        lmax = process_counter
        lmaxind = dat[1]
    
    
max_start_time = data2[lmaxind][0]  
max_end_time = 0      
for i in range(lmaxind, len(data2)):
    if not data2[i][2]:
        max_end_time = data2[i][0]
        break
    

print(lmax, max_end_time-max_start_time)

print(data2[lmaxind:lmaxind+10])