import turtle as t
t.left(90)
t.speed(1000)
k=10
t.down()
for i in range(3):
    t.forward(7*k)
    t.right(90)
t.forward(8*k)
for i in range(3):
    t.left(90)
    t.forward(5*k)
t.up()
for x in range(-1, 8):
    for y in range(-5, 8):
        t.goto(x*k,y*k)
        t.dot('red')

input()