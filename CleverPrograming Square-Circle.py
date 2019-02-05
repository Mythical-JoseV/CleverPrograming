import turtle

Turtle = turtle.Turtle()
Turtle.speed(0)

def square(length, angle):
    Turtle.forward(length)
    Turtle.right(angle)
    Turtle.forward(length)
    Turtle.right(angle)
    Turtle.forward(length)
    Turtle.right(angle)
    Turtle.forward(length)
    Turtle.right(angle)

def circle():
    for i in range(400):
        square(200,90)
        Turtle.right(1)

square(100,90)
circle()
