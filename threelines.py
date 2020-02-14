import turtle

# Instantiate a new Turtle Object
wn = turtle.Screen()
box = turtle.Turtle()

box.pensize(3)

box.penup()
box.fd(40)
box.pendown()
box.fd(200)

# turning up
box.penup()
box.right(90)
box.fd(30)
box.right(90)
box.pendown()
box.fd(200)

# turning up
box.penup()
box.left(90)
box.fd(30)
box.left(90)
box.pendown()
box.fd(200)
box.left(90)
wn.exitonclick()
