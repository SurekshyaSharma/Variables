import turtle

s_turtle = turtle.Turtle()
s_turtle.speed(10)


def hexagon():
    s_turtle.fillcolor('black')
    s_turtle.begin_fill()
    s_turtle.begin_fill()
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.forward(100)
    s_turtle.right(100)
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.forward(100)
    s_turtle.right(400)
    s_turtle.forward(100)
    s_turtle.right(100)
    s_turtle.forward(100)
    s_turtle.end_fill()
    s_turtle.penup()
    s_turtle.forward(30)
    # s_turtle.right(100)
    # s_turtle.forward(100)
# pinwheel

for i in range(9):
    hexagon()
s_turtle.pendown()

screen = turtle.Screen()
screen.exitonclick()




