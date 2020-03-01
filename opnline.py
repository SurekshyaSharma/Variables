import turtle as t


def draw_line(a_turtle):
    a_turtle.pendown()
    a_turtle.forward(200)
    a_turtle.penup()
    a_turtle.back(200)

def main():
    pass
    # your main function here
    wn = t.Screen()
    moxie = t.Turtle()

    start_x = int(input("Enter starting X position: "))
    start_y = int(input("Enter starting Y position: "))
    start_heading = int(input("Enter starting heading direction: "))

    moxie.penup()
    # setting the direction and call it back to its original position
    moxie.setx(start_x)
    moxie.sety(start_y)
    moxie.setheading(start_heading)

    draw_line(moxie)  # makes easier ge the shortcut which saves the typing

    wn.exitonclick()


main()
