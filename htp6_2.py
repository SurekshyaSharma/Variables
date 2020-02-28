import turtle


HYPOTENUSE = (2 ** 0.5) / 2

wn = turtle.Screen()


square = turtle.Turtle()

square.setheading(45)
square.width(3)

for radius in range(20, 20 * 50 + 1, 20):
    square.penup()
    square.goto(radius/2, -radius/2)
    square.pendown()
    square.circle(radius * HYPOTENUSE, steps=4)

wn.exitonclick()
