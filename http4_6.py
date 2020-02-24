import turtle

s_turtle = turtle.Turtle()
s_turtle.speed(10)

sides = int(input("Enter the number of the sides:"))
length = int(input("Enter the length of the sides:"))

color_outline = (input("Enter the outline color:"))

color_fill = (input("Enter the filling color:"))
angle = 360/sides
print(angle)

s_turtle.color(color_outline)
s_turtle.fillcolor(color_fill)
s_turtle.begin_fill()
for i in range(sides):
    s_turtle.forward(length)
    s_turtle.left(angle)
s_turtle.end_fill()

screen = turtle.Screen()
screen.exitonclick()

