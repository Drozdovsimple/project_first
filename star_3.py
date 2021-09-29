import turtle


n = 7
angle = (180-360/n)/3                                           
turtle.speed(6)

while True:
    turtle.forward(100)
    turtle.left(180-angle)
    if abs(turtle.pos()) < 1:
        break
    
turtle.mainloop() 
print(angle)
