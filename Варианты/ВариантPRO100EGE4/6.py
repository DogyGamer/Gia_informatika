from turtle import *

k = 20

speed(1000)

f = lambda x: forward(k*x)
r = lambda x: right(x)
l = lambda x: left(x)


for _ in range(3):
    pendown()
    for _ in range(2):
        f(7)
        r(90)
        f(7)
        r(90)
    penup()
    
    f(6)
    r(90)
    f(6)
    l(90)


for x in range(0,19+1):
    for y in range(-19, 0+1):
        penup()
        setpos(k*x, k*y)
        pendown()
        dot()
    
    
input()

