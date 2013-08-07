# This is where Exercise 5.4 goes
# Name: Cassie Sancartier

#1

def is_triangle(a, b, c):
	if a + b <= c or b + c <= a or a + c <= b:
		print "No"
	else:
		print "Yes"

		
is_triangle(10, 12, 15)
Yes

is_triangle(1, 2, 15)
No


#2

def user_defined_triangle():
	"""Will three sticks with lengths defined by a user be able to form a triangle?"""
	a = raw_input('How long is the first stick?\n')
	b = raw_input('How long is the second stick?\n')
	c = raw_input('How long is the third stick?\n')
	is_triangle(int(a), int(b), int(c))

