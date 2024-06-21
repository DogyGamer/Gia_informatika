from turtle import *

k = 30

speed(500)

r = lambda x: right(x)
f = lambda x: forward(k*x)

r(135)
for _ in range(7):
    f(7)
    r(45)
    f(8)
    r(135)
    
for x in range(-15, 5):
    for y in range(-10, 5):
        penup()
        setpos(k*x,k*y)
        pendown()
        dot()
        penup()

input()
