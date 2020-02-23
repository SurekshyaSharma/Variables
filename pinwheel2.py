import turtle

wn = turtle.Screen()
s_turtle = turtle.Turtle()
s_turtle.speed(30)


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
    s_turtle.color("black")
    s_turtle.forward(100)


# pinwheel
for i in range(9):
    hexagon()

s_turtle.penup()
s_turtle.right(90)
s_turtle.forward(170)
s_turtle.pendown()
s_turtle.forward(180)


s_turtle.right(270)
s_turtle.forward(10)
s_turtle.left(90)
s_turtle.forward(190)
# s_turtle.end_fill()

s_turtle.penup()
s_turtle.right(270)
s_turtle.forward(300)
s_turtle.right(90)
s_turtle.pendown()
s_turtle.forward(400)
s_turtle.right(90)
s_turtle.forward(600)
s_turtle.right(90)
s_turtle.forward(600)
s_turtle.right(90)
s_turtle.forward(600)
s_turtle.right(90)
s_turtle.forward(200)
s_turtle.left(90)

# side border
s_turtle.penup()
s_turtle.forward(20)
s_turtle.right(90)
s_turtle.pendown()
# s_turtle.fillcolor('black')
# s_turtle.begin_fill()
s_turtle.forward(420)
s_turtle.right(90)
s_turtle.forward(640)
s_turtle.right(90)
s_turtle.forward(640)
s_turtle.right(90)
s_turtle.forward(640)
s_turtle.right(90)
s_turtle.forward(220)
# border decoration


def border_style():
    s_turtle.right(120)
    s_turtle.forward(20)
    s_turtle.right(120)
    s_turtle.forward(20)
    s_turtle.right(120)
    s_turtle.forward(20)

    
border_style()
# border_style()

wn.exitonclick()


