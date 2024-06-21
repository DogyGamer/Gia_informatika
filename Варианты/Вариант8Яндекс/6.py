from turtle import *
k = 40
speed(10000)
f = lambda x: forward(k*x)
r = lambda x: right(x)
l = lambda x: left(x)
pendown()
right(30)
for _ in range(3):
    r(45)
    f(4)
    r(45)   
r(315)
f(4)
for _ in range(2):
    r(90)
    f(4)
for x in range(-5, 2):
    for y in range(-5, 5):
        penup()
        setpos(k*x, k*y)
        pendown()
        dot()      
input()