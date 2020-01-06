import turtle
a = 5
print(a)

b = "hello"
print(b)

#square
s_turtle = turtle.Turtle()

def square():
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)

#1stSquare
square()
s_turtle.right(90)
s_turtle.forward(100)
square()
s_turtle.forward(100)
 #2nd square
square()
square() 
#3rd
s_turtle.right(180)
s_turtle.forward(200)
square()
square()
#4th
s_turtle.right(180)
s_turtle.forward(200)
square()
square()
# filling the block
square()
square()
s_turtle.right(180)
s_turtle.forward(200)
square()
square()
s_turtle.right(180)
s_turtle.forward(200)
square()
square()