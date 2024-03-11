import turtle as t

k = 10

for i in range(2):
    t.pendown()
    t.forward(k*9)
    t.right(90)
    t.forward(k*15)
    t.right(90)
    
t.penup()
t.forward(k*12)
t.right(90)
t.pendown()

for i in range(2):
    t.pendown()
    t.forward(k*6)
    t.right(90)
    t.forward(k*12)
    t.right(90)
    

t.goto(0,0)    
t.pencolor(1,0,0)
for y in range(20):
    for x in range(20):
        t.penup()
        t.forward(k)
        t.pendown()
        t.dot(6)
    if y % 2 == 0:
        t.penup()
        t.left(90)
        t.forward(k)
        t.left(90)
    else:
        t.penup()
        t.right(90)
        t.forward(k)
        t.right(90)
    
input()


