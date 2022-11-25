import turtle

t = turtle.Turtle()
s = t.getscreen()
turtle.bgcolor('black')

t.color('orange')

t.penup()

t.speed(0.4)
b = 45
for i in range(500):
    t.pendown()
    t.forward(15 + i)
    t.right(91)

turtle.done()

