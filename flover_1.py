import turtle

angle = 60
radius = 30
for step in range(3):
    turtle.circle(radius)
    turtle.circle(-radius)
    turtle.setheading(angle)
    angle += 60
turtle.mainloop()
