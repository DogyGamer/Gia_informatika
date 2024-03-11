import turtle as t
k = 27
t.speed(100)
# Направо 60 Вперёд 4 Направо 120
# Повтори 4 [Вперёд 3 Направо 240 Вперёд 3 Направо 120]
# Вперёд 4 Направо 90 Вперёд 8383
# ​ Направо 90 Вперёд 8.

t.right(60)
t.forward(k*4)
t.right(120)

for _ in range(4):
    t.forward(k*3)
    t.right(240)
    t.forward(k*3)
    t.right(120)

t.forward(4*k)
t.right(90)
t.forward(k*( 8*(3**0.5) ))
t.right(90)
t.forward(k*8)


for x in range(5, -10,-1):
    for y in range(0, -15, -1):
        print(x,y)
        t.penup()
        t.setpos(k*x, k*y)
        t.pendown()
        t.dot(6)
input()