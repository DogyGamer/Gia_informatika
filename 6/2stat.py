import turtle
k = 10

c=0

for i in range(3):
    for _ in range(7):
        c+=1
        turtle.dot(k*0.5)
        turtle.forward(k)
        
    turtle.right(90)

for _ in range(10):
    c+=1
    turtle.dot(k*0.5)
    turtle.forward(k)
    

for i in range(3):
    turtle.left(90)
    for _ in range(6):
        c+=1
        turtle.dot(k*0.5)
        turtle.forward(k)

print(c)
input()
