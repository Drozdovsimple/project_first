import turtle 

turtle.speed(1)
n = 12
angle = -360/n
for i in range(n):
    turtle.rt(angle)
    turtle.fd(100)
    turtle.stamp()
    turtle.rt(180)
    turtle.fd(100)
    turtle.rt(180)
turtle.done() # сделано

