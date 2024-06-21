from turtle import *

speed(1000)

x = 0
y = 0

k = 25

ops = [[0,2], [2,0], [0, 10], [-2,0], [0,2], [6,0], [0,-2], [-2,0], [0,-10], [2,0], [0,-2], [-6,0]]


for _ in range(5):
    for x2, y2 in ops:
        x += x2
        y += y2
        
        setpos(k*x,k* y)


for x in range(0, 7):
    for y in range(0, 15):
        penup()
        setpos(k*x,k*y)
        pendown()
        dot()
        

input()
