from turtle import *

k = 0.8

f = lambda x: forward(k*x)
r = lambda x: right(x)
pd = lambda: pendown()
pu = lambda: penup()

speed(500)

# pu()

# r(270)
# f(350)
# r(270)
# f(50)
# r(180)

pd()

for _ in range(20):
    f(53)
    r(90)
    f(38)
    r(90)

pu()

r(90)
f(1)
r(90)
f(2)
r(270)

pd()

for _ in range(32):
    f(83)
    r(270)
    f(53)
    r(270)
    
        

input()