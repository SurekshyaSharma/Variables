def draw_line_from(x,y,h,the_turtle):

    the_turtle.penup()

    original_x = the_turtle.xcor()
    original_y = the_turtle.ycor()
    original_heading = the_turtle.heading()
    # setting the direction and call it back to its original position
    the_turtle.setx(x)
    the_turtle.sety(y)
    the_turtle.setheading(h)

    draw_line(the_turtle)
    the_turtle.setx(original_x)
    the_turtle.sety(original_y) # draw the line and bring it back how it was there
    the_turtle.setheading(original_heading)

# make a copy of oneline.py here,
import turtle as t


def draw_line(a_turtle):
    a_turtle.pendown()
    a_turtle.forward(200)
    a_turtle.penup()
    a_turtle.back(200)


def main():
    wn = t.Screen()
    moxie = t.Turtle()
    t.stamp() # show the home position
    moxie.speed(0)
    start_x = int(input("Enter starting X position: "))
    start_y = int(input("Enter starting Y position: "))
    start_heading = int(input("Enter starting heading direction: "))

    for count in range(30):
        draw_line_from(start_x, start_y,start_heading,moxie)  # makes easier ge the shortcut which saves the typing
        # draw_line_from(start_x, start_y, start_heading+30, moxie)
        start_heading = start_heading + 12

    wn.exitonclick()


main()
