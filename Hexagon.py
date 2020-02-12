import turtle

wn = turtle.Screen()
# square
s_turtle = turtle.Turtle()
s_turtle.speed(10)
s_turtle.fillcolor('pink')
s_turtle.begin_fill()


# Hex-Shape
def hexagon():
    s_turtle.pensize(2)
    s_turtle.color("red")
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.color("orange")
    s_turtle.forward(100)
    s_turtle.right(100)
    s_turtle.color("green")
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.color("yellow")
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.color("blue")
    s_turtle.forward(100)
    s_turtle.right(100)
    s_turtle.color("violet")
    s_turtle.forward(100)


# pinwheel

hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
s_turtle.end_fill()
wn.exitonclick()
