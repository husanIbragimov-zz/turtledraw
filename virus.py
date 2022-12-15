from turtle import *
bgcolor('black')

penup()
left(90)
forward(70)
right(90)
forward(380)
pendown()
speed(13)
color('green')
b = 200
while b > 0:
    left(b)
    forward(b * 4)
    b = b - 1

done()
