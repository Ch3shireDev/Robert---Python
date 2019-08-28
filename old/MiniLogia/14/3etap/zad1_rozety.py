from turtle import *

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


def skok(a,b=0):
    pu();
    fd(a);rt(90);
    fd(b);lt(90)
    pd()

def kat10(a):
    for i in range(10):
        fd(a);rt(36)

def kat8(a):
    for i in range(8):
        fd(a);lt(45)        


def mala(a):
    for i in range(8):
        kat8(a)
        skok(2*a)
        lt(45)
    
def rozety():
    a = 28
    lt(72)
    for i in range(5):
        mala(a)
        kat10(a)
        skok(2*a)
        rt(36)
        kat10(a)
        skok(2*a)
        rt(36)

 




