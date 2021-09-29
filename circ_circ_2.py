import turtle

n = 2
t=turtle.Turtle()
for i in range(10):
    t.circle(i*15, None, n)
    t.penup()
    t.setposition(0,-(i*15))
    t.pendown()
    n +=1
turtle.done()
