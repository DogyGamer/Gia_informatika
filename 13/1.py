# 255.255.255.192
a = bin(192)[2:] #смотрим кол-во нулей в двоич записи числа
b = a.count("0")
print(2**b - 2) # Находим кол-во возоможных вариаций адресов и исключаем два по условию