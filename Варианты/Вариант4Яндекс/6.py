from turtle import *

k = 120
speed(100)
f = lambda x: forward(k*x) 
r = lambda x: right(x)

for i in range(36):
    f(1)
    r(36)
    
penup()

f(4)
r(90)

pendown()

for _ in range(8):
    f(6)
    r(90)

for x in range(-3, 3):
    for y in range(-3, 1):
        penup()
        setpos(k*x,k*y)
        pendown()
        dot(6)

input()