import turtle
import time
from matplotlib import pyplot as plt


def DrawBox():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    t.right(24)
    t.forward(80)
    t.right(132)
    t.forward(80)
    position = t.pos()
    t.left(66)
    t.forward(80)
    t.right(66)
    t.backward(80)
    t.left(66)
    t.backward(80)
    t.right(66)
    t.forward(80)
    t.left(66)
    t.forward(80)
    t.right(113)
    t.forward(80)
    t.right(66)
    t.forward(80)
    t.right(113)
    t.forward(80)
    t.backward(80)
    t.left(48)
    t.forward(80)
    return position

def MoveTurtle(turt, position):
    turt.penup()
    turt.goto(position)
    turt.pendown()

def DrawCat(position, frame, is_last=False):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    num = frame/10
    trueNum = 1+num

    MoveTurtle(t, position)

    t.fillcolor("orange")
    t.begin_fill()
    circSize = 15* trueNum
    t.circle(circSize, 144)
    x1 = t.xcor()
    y1 = t.ycor()
    t.circle(circSize, 36)
    x3 = t.xcor()
    y3 = t.ycor()
    t.circle(circSize, 36)
    x2 = t.xcor()
    y2 = t.ycor()
    t.circle(circSize, 144)
    t.end_fill()


    MoveTurtle(t, (x1,y1 +(circSize*0.875)))
    t.begin_fill()
    t.circle(-(7.5*trueNum), steps=3)
    MoveTurtle(t, (x2, y2 +(circSize*0.875)))
    t.circle(-(7.5*trueNum), steps=3)
    t.end_fill()

    MoveTurtle(t, ((x1-circSize*0.1), y1 - (circSize*0.6)))
    t.fillcolor("black")
    t.begin_fill()
    t.circle((circSize*0.066))
    MoveTurtle(t, ((x2+circSize* 0.1), y2 - (circSize*0.6)))
    t.circle((circSize*0.066))
    t.end_fill()

    MoveTurtle(t, (x3, (y3-circSize*1.1)))
    t.fillcolor("black")
    t.begin_fill()
    t.circle((circSize*0.066), steps=3)
    t.end_fill()



    MoveTurtle(t, (x3, (y3-circSize*1.1)))
    t.left(23)
    t.forward(circSize*0.5)
    t.backward(2*(circSize*0.5))
    MoveTurtle(t, (x3, (y3-circSize*1.1)))
    t.right(23)
    t.forward(circSize*0.5)
    t.backward(2*(circSize*0.5))
    MoveTurtle(t, (x3, (y3-circSize*1.1)))
    t.right(23)
    t.forward(circSize*0.5)
    t.backward(2*(circSize*0.5))

    if not is_last:
        t.clear()

if __name__ == '__main__':
    pos = DrawBox()

    for i in range(30):
        DrawCat(pos, i, is_last=(i == 29))
    turtle.done()   

