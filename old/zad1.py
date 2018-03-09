import turtle as t
from math import sqrt

alpha = 60
width = 600

def rombA(a):
    global alpha
    t.fillcolor('dark grey')
    t.begin_fill()
    for _ in range(2):
        t.fd(a)
        t.rt(alpha)
        t.fd(a)
        t.rt(180-alpha)
    t.end_fill()

def rombB(a):
    global alpha
    t.fillcolor('light grey')
    t.begin_fill()
    for _ in range(2):
        t.fd(a)
        t.lt(alpha)
        t.fd(a)
        t.lt(180-alpha)
    t.end_fill()

def cube(a):
    global alpha
    rombA(a)
    rombB(a)  
    t.lt(alpha)  
    t.fd(a)
    t.rt(alpha)
    t.fd(a)
    for i in range(2):
        t.rt(alpha)
        t.fd(a)
    t.rt(alpha)
    t.fd(a)
    t.rt(alpha)
    t.fd(a)
    t.rt(180-alpha)

def cubes_row(a, n):
    global alpha
    for i in range(n):
        t.pendown()
        cube(a)
        t.penup()
        t.rt(alpha)
        t.fd(a)
        t.rt(alpha)
        t.fd(a)
        t.lt(2*alpha)
    # for i in range(n):
    t.lt(alpha)
    t.fd(a)
    for i in range(n):
        t.lt(alpha)
        t.fd(a)
        t.rt(alpha)
        t.fd(a)
    t.rt(alpha)
    #     t.lt(alpha)
    #     t.fd(a)

def cubes_tower(n):
    global alpha, width
    t.penup()
    a = width/sqrt(3)/n
    height = a*(n+sqrt(3)/4*(2*n-3))
    t.goto(-a*sqrt(3)/4*(2*n-2),-height/2-3*a/4)
    t.lt(90)
    for i in range(n):
        cubes_row(a,n-i)
        t.fd(a)
        t.rt(alpha)
        t.fd(a)
        t.rt(alpha)
        t.fd(a)
        t.lt(2*alpha)
    t.penup()
    # t.goto(-width/2,-height/2)
    # t.pendown()
    # t.goto(width/2,-height/2)
    # t.goto(width/2,height/2)
    # t.goto(-width/2,height/2)
    # t.goto(-width/2,-height/2)
    t.hideturtle()

n = 4

t.speed(0)
cubes_tower(7)

t.done()