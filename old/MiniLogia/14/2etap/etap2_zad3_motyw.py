from turtle import *

#funkcja testuj() do testowania rozwiązania
def testuj(n):
    a=499
    b=796
    reset()

    tracer(0)
    if n==1:
        kwiat()
    if n==2:
        tetki(2)
    if n==3:
        motyw(3)
    
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

#zadanie 3, etap 2, miniLOGIA 14

def motyw(n):
    #wyliczenie długości boku
    a = 450/(6*n)
    lt(90)
    #wyśrodkowanie rysunku
    skok(-3*a,-4*n*a+2*a)
 
    #lewa część
    for i in range(1,n+1):
        for j in range(i):
            elt(a)
            skok(6*a)
        skok(-6*a*i-3*a,4*a)
        
    skok(6*a)

    #prawa część
    for i in range(1,n):
        for j in range(n-i):
            elt(a)
            skok(6*a)
        skok(-6*a*(n-i-1)-3*a,4*a)


def elt(a):
    #żółto-niebieski element
    fillcolor("blue")
    prost(6*a,4*a)
    skok(2*a,a)

    fillcolor("white")
    prost(2*a,2*a)
    skok(-2*a,-a)

    fillcolor("yellow")
    prost(a,a)
    skok(5*a,0)
    prost(a,a)
    skok(0,3*a)
    prost(a,a)
    skok(-5*a,0)
    prost(a,a)
    skok(0,-3*a)

def prost(a,b):
    begin_fill();
    for i in range(2):
        fd(a);rt(90)
        fd(b);rt(90)
    end_fill()


def skok(a,b=0):
    pu()
    fd(a); rt(90)
    fd(b); lt(90)
    pd()

