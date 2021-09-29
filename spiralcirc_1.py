import turtle

def spcirc(rb, rm, n):# rb big radius#
	for step in range(n):
	    turtle.setheading(90)
	    turtle.circle(-rb, 180)
	    turtle.circle(-rm, 180)  
	turtle.circle(-rb, 180)


spcirc(30, 20, 3)
turtle.mainloop()
