

def genStr(in_str):
    or_str = in_str
    while '21' in or_str or '31' in or_str or '32' in or_str:
        if '21' in or_str:
            or_str = or_str.replace('21', '12')
        if '31' in or_str:
            or_str = or_str.replace('31', '13')
        if '32' in or_str:
            or_str = or_str.replace('32', '23')

    return or_str


# for i in range(0,100000, 1):
#     stri = ""
#     for j in range(i):
#         if(j % 3 == 0):
#             stri += "1"
#         if(j % 3 == 1):
#             stri += "2"
#         if(j % 3 == 2):
#             stri += '3'

#     res = genStr(stri)
#     if len(res) >= 50:
#         if res[49] == 2:
#             print("POBEDAAAA: ", i)

# stri = ""
# i = 75
# for j in range(i):
#     if(j % 3 == 0):
#         stri += "1"
#     if(j % 3 == 1):
#         stri += "2"
#     if(j % 3 == 2):
#         stri += '3'

# res = genStr(stri)
# print(res)



for i in range(3, 150):
    c_1 = i // 3
    c_2 = i // 3
    c_3 = i // 3
    if(i % 3 == 1):
        c_1 += 1
    if(i % 3 == 2):
        c_1 += 1
        c_2 += 1
    gendstr = "1"*c_1 + "2"*c_2 + "3"*c_3
    if(len(gendstr) >= 50):
        if(gendstr[49] == "2"):
            print("POBEDA SUKA BLYYA: ", i)
# print('\n')
# print(res[49])
# print('\n')
# print(res.count("1"))

