import turtle

#square
s_turtle = turtle.Turtle()
s_turtle.speed(10)

def square():
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)
  s_turtle.right(90)
  s_turtle.forward(100)

# #1stSquare
# square()
# s_turtle.right(90)
# s_turtle.forward(100)
# square()
# s_turtle.forward(100)
#  #2nd square
# square()
# square() 
# #3rd
# s_turtle.right(180)
# s_turtle.forward(200)
# square()
# square()
# #4th
# s_turtle.right(180)
# s_turtle.forward(200)
# square()
# square()
# # filling the block
# square()
# square()
# s_turtle.right(180)
# s_turtle.forward(200)
# square()
# square()
# s_turtle.right(180)
# s_turtle.forward(200)
# square()
# square()
print ("-" * 25)

#if else statement 
print(3>2)
print ("-" * 25)
a_value = 3
b_value = 4
if a_value > b_value:
  square()
else:
  print("Hello")
print ("-" * 25)

# # square within a loop
# numbers = [1,2,2,3,4,5,6,7,8]
# for x in numbers:
#   print(x)
#   if x == 4:
#     break
#   square()
#   s_turtle.right(180)
#   s_turtle.forward(100)

# Hexa shape 
def hexagon():
  s_turtle.forward(100)
  s_turtle.right(400)
  s_turtle.forward(100)
  s_turtle.right(100)
  s_turtle.forward(100)
  s_turtle.right(400)
  s_turtle.forward(100)
  s_turtle.right(400)
  s_turtle.forward(100)
  s_turtle.right(100)
  s_turtle.forward(100)

hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()
hexagon()