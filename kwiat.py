import turtle as t

def part1(x=8):
    t.penup()
    t.forward(x)
    t.pendown()
    t.begin_fill()
    t.forward(4*x)
    t.left(60)
    t.forward(4*x)
    t.right(120)
    t.forward(4*x)
    for i in range(3):
        t.right(60)
        t.forward(4*x)
    t.end_fill()
    t.penup()
    t.left(60)
    t.forward(x)
    t.left(180)

def part2(x=8):
    for i in range(6):
        part1(x)
        t.right(60)
    t.penup()

def part3(x=8):
    t.left(30)
    part2(x)
    for i in range(6):
        t.penup()
        t.forward(19*x)
        part2(x)
        t.backward(19*x)
        t.left(60)


t.hideturtle()
t.color("black", "yellow")
t.speed(0)
part3()

cv = t.getcanvas()
cv.postscript(file="kwiat.ps", colormode='color')
