#Imports and there set up
import turtle
import random

Turtle = turtle.Turtle()
Turtle.speed(0)
random = random.randint(0,50)
turtle.bgcolor('black')



#Functions
def art():
    square(random, random)
    Turtle.forward(90)
    

def square(length, angle):
    Turtle.forward(length)
    Turtle.left(angle)
    Turtle.forward(length)
    Turtle.right(angle)
    Turtle.forward(length)
    Turtle.left(angle)
    Turtle.forward(length)
    Turtle.left(angle)

def cirlce():
    square(50,90)
    Turtle.forward(1)
    Turtle.right(1)

def art2():
    Turtle.right(90)
    Turtle.forward(100)
    for i in range(15):
        art()
        Turtle.color('red')

    Turtle.forward(60)

    for i in range(300):
        cirlce()
        Turtle.color('orange')

    for i in range(15):
        art()
        Turtle.color('honeydew')

    Turtle.forward(100)

    for i in range(300):
        cirlce()
        Turtle.color('yellow')
    Turtle.forward(50)

    for i in range(15):
        art()
        Turtle.color('cyan')

    Turtle.forward(100)

    for i in range(300):
        cirlce()
        Turtle.color('maroon')

    Turtle.forward(100)

    for i in range(15):
        art()
        Turtle.color('indigo')

    Turtle.forward(50)

    for i in range(300):
        cirlce()
        Turtle.color('Peru')
        
    Turtle.forward(100)

    for i in range(15):
        art() 
        Turtle.color('Crimson')
    Turtle.forward(100)

    for i in range(300):
        cirlce()
        Turtle.color('fuchsia')
        
    Turtle.forward(random)

    for i in range(15):
        art()
        Turtle.color('moccasin')
        
    Turtle.forward(100)

    for i in range(300):
        cirlce()
        Turtle.color('purple')

#Art
art2()
Turtle.goto(0,0)
art2()
Turtle.goto(200,0)
art2()
