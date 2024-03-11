import turtle as t
t.speed(100)

k=30

t.penup()

t.right(30)
t.forward(k*4)
t.right(330)
t.pendown()

t.forward(k*4)
t.right(90)
t.forward(k*7)
t.right(45)
t.forward(k*(4*(2**0.5)))
t.right(135)
t.forward(k*11)

for x in range(2,9):
    for y in range(-1,-15, -1):
        t.penup()
        t.setpos(x*k, y*k)
        t.pendown()
        t.dot(7)
        



input()