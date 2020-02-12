import turtle

# Instantiate a new Turtle Object
wn = turtle.Screen()
box = turtle.Turtle()

box.pensize(3)
box.stamp()

box.penup()
box.fd(40)
box.pendown()
box.left(90)
box.fd(40)
box.left(90)
# # Inner circle

box.fd(80)
box.left(90)
box.fd(80)
box.left(90)
box.fd(80)
box.left(90)
box.fd(40)

# # Outer circle
box.penup()
box.right(90)
box.fd(10)
box.left(90)
box.pendown()
box.fd(50)
box.left(90)
box.fd(100)
box.left(90)
box.fd(100)
box.left(90)
box.fd(100)
box.left(90)
box.fd(50)

wn.exitonclick()
