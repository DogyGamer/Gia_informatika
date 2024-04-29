from turtle import *

speed(100)

k = 30

fwd = lambda x: forward(k*x)
r = lambda x: right(x)

for _ in range(6):
    fwd(7)
    r(120)

penup()

fwd(3)
r(90)
pendown()

for _ in range(8):
    fwd(5)
    r(90)
    
    
    
for x in range(-3, 8, 1):
    for y in range(-7, 1):
        penup()
        setpos(x*k,y*k)
        pendown()
        dot(5)
input()