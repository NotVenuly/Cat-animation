import turtle
import time


def DrawBox():
    t = turtle.Turtle()

    t.right(24)
    t.forward(80)
    t.right(132)
    t.forward(80)
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


if __name__ == '__main__':
    DrawBox()
    turtle.done()   

