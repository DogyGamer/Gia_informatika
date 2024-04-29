from turtle import *

k = 20

r = lambda x: right(x)
l = lambda x: left(x)
fwd = lambda x: forward(x*k)

speed(100)

for _ in range(2):
    fwd(13)
    r(90)
    fwd(18)
    r(90)

penup()
fwd(5)
r(90)
fwd(9)
l(90)

pendown()

for _ in range(2):
    fwd(11)
    r(90)
    fwd(7)
    r(90)
    


for x in range(0, 16):
    for y in range(-9, -17, -1):
        penup()
        setpos(x*k,y*k)
        pendown
        dot()
        
input()