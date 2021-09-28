from turtle import *


def circ(r, pcol, fcol):
	pencolor(pcol)
	fillcolor(fcol)
	begin_fill()
	circle(r)
	end_fill()
rad = 70
speed(6)
up()
goto(rad, 0)
lt(90)
down()
circ(rad, 'black', 'yellow')
up()
goto(-rad/3, rad/3)
circ(10, 'black', 'blue')
up()
goto(rad/3, rad/3)
circ(-10, 'black', 'blue')
up()
goto(0, 10)
down()
pensize(5)
pencolor('black')
fillcolor('black')
bk(25)
up()
goto(rad/2.5, -25)
lt(180)
down()
pensize(7)
pencolor('red')
circle(-rad/2.5, 180)

done()

#coment



	    
