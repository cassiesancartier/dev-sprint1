## Exercise 5.6
## Name: Cassie Sancartier

world.clear()
bob = Turtle()


def koch(turtle, length):
	if length < 3:
		fd(turtle, length)
	else:	
	    fd(turtle, (length / 3))
	    lt(turtle, 60)
	    fd(turtle, (length / 3))
	    rt(turtle, 120)
	    fd(turtle, (length / 3))
        lt(turtle, 60)
        fd(turtle, (length / 3))
        lt(turtle, 60)
     
     
def snowflake(turtle, length):
	for i in range(3):
	    koch(turtle, length)
	    rt(turtle, 180)


def quadratic_curve(turtle, length):	
    if length < 5:
		fd(turtle, length)
		return
	else:	
	    fd(turtle, (length / 5))
	    lt(turtle, 90)
	    fd(turtle, (length / 5))
	    rt(turtle, 90)
	    fd(turtle, (length / 5))
        rt(turtle, 90)
        fd(turtle, (length / 5))
        lt(turtle, 90)
        fd(turtle, (length / 5))


