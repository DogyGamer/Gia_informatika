from turtle import *

pu = lambda : penup()
pd = lambda : pendown()

d = lambda : dot()
speed(2000)
k = 15

f = lambda x: forward(k*x)
r = lambda x: right(x)
l = lambda x: left(x)

for _ in range(2):
    f(10)
    r(90)
    f(18)
    r(90)
    
pu()

f(5)
r(90)
f(14)
l(90)

pd()

for _ in range(2):
    f(17)
    r(90)
    f(7)
    r(90)
    
for x in range(5,11):
    for y in range(-18, -13):
        pu()
        setpos(k*x, k*y)
        pd()
        d()
        
input()