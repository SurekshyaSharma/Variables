import turtle as t
def draw_three_lines(the_turtle):
    pass

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



def draw_line(a_turtle):
    a_turtle.pendown()
    a_turtle.forward(200)
    a_turtle.penup()
    a_turtle.back(200)


def main():
    wn = t.Screen()
    larry = t.Turtle()
    draw_line_from(0,0,90,larry)
    draw_line_from(30, 0, 90,larry)
    draw_line_from(60, 0, 90,larry)

    wn.exitonclick()


main()
