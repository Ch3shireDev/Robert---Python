from turtle import *
from math import sqrt

#funkcja testuj() do testowania rozwiązania
def testuj(n):
    a=499
    b=796
    reset()
    pd()
    color("black")

    tracer(0)
    if n==1:
        rozety()
    if n==2:
        lampki(8)
    if n==3:
        serweta(2)
    
    pu(); home(); pd()
    pu();fd(b/2);pd()
    lt(90)
    color("red")
    for i in range(2):
        fd(a//2);lt(90)
        fd(b);lt(90)
        fd(a//2)
    rt(90)
    pu();bk(b/2);pd()
    color("black")
    update()

    tracer(1)
    if n==1:
        addshape("zad1.gif")
    if n==2:
        addshape("zad2.gif")
    if n==3:
        addshape("zad3.gif")   
    zolw_test = Turtle()
    if n==1:
        zolw_test.shape("zad1.gif")
    if n==2:
        zolw_test.shape("zad2.gif")
    if n==3:
        zolw_test.shape("zad3.gif")
    zolw_test.speed(0)
    zolw_test.pu()
    zolw_test.ondrag(zolw_test.goto)


#tutaj jest miejsce na Twoje rozwiązania zadania


def deltoid(a):
    b = a / sqrt(2)
    lt(30)
    fillcolor("green")
    begin_fill()
    fd(a);rt(75)
    fd(b);rt(90)
    fd(b);rt(75)
    fd(a);rt(120)
    end_fill()
    rt(30)
    

def ramie(a,n):
    if n==1:
        deltoid(a)
    else:
        b = a / sqrt(2)
        lt(30)
        fd(a);lt(60)
        ramie(a / 2,n - 1)
        rt(135)
        fd(b)
        lt(45)
        ramie(a / 2,n - 1)
        rt(135)
        fd(b)
        lt(45)
        ramie(a / 2,n - 1)
        rt(120)
        fd(a)
        rt(150)
        deltoid(a)


def serweta(n):
    fd(65/2)
    ramie(130,n)
    rt(180)
    fd(65)
    ramie(130,n)

