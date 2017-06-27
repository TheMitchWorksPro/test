# this is a sample Python file
# this draws something very simple
# this sample drew a square
# it may have been modified since that initial idea ...

import turtle

painter = turtle.Turtle()
painter.pensize(15)

for _ in range(24):
    painter.forward(100)
    painter.left(100)

turtle.done()

