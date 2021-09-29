import turtle

radius = 30
for step in range(10):
    turtle.setheading(90)
    turtle.circle(radius)
    turtle.circle(-radius)
    radius += 5
turtle.mainloop()
