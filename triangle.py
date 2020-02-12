import turtle

t = turtle.Turtle()
t.pensize(2)
t.forward(100)  # draw base

t.left(120)
t.forward(100)

t.left(120)
t.forward(100)
t.left(120)
# smaller triangle
t.forward(50)
t.left(120)
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)

turtle.done()
