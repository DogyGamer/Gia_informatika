from turtle import *

k = 20

f = lambda x: forward(k*x)
r = lambda x: right(x)
l = lambda x: left(x)

speed(200)

for _ in range(2):
    f(12)
    r(90)
    f(19)
    r(90)
    
penup()

f(4)
r(90)
f(6)
l(90)

pendown()

for _ in range(2):
    f(12)
    r(90)
    f(6)
    r(90)
    
    
for x in range(4, 15):
    for y in range(-6, -15, -1):
        penup()
        setpos(k*x,k*y)
        pendown()
        dot()
        
# 7*9
    
input()