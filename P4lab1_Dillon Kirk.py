# Dillon Kirk
# 22 Nov 2025
# P4lab1
# Use turtle and loops to draw a square and triangle

import turtle

win = turtle.Screen()
pen = turtle.Turtle()

pen.pensize(5)
pen.pencolor("red")
pen.shape("turtle")

for side in range(6):
    pen.forward(100)
    pen.left(90)

sides = 3

while sides > 0:
    pen.pencolor("blue")
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.forward(100)
    pen.right(120)
    sides = sides - 1
    pen.end_fill()
    
win.mainloop()