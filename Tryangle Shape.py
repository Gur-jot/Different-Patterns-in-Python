# import the turtle modules
import turtle


# define the function
# for triangle
def form_tri(side):
	for i in range(3):
		my_pen.fd(side)
		my_pen.left(120)
		side -= 10

		
# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("white")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("black")

tut = turtle.Screen()		

# for different shapes
side = 300
for i in range(10):
	form_tri(side)
	side -= 30
