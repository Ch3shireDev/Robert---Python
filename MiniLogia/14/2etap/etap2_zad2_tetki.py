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

#zadanie 2 miniLOGIA 14

def tetki(n):
    #zmienna pomocnicza
    a = 10
    #wyśrodkowanie rysunku
    skok(a/2,-a/2)
    #ramki
    for i in range(n):
        ramka(i+1,a)
        skok(3*a,-3*a)


def litera_t(a):
    fillcolor("olive");
    begin_fill();
    fd(a); lt(90); fd(a); rt(90)
    fd(a); rt(90); fd(3*a); rt(90)
    fd(a); rt(90); fd(a); lt(90)
    fd(a); rt(90); fd(a); rt(90)
    end_fill();


def ramka(n,a):
    #pojedyncza ramka
    for i in range(4):
        rzad(n,a)
        rt(90)


def rzad(n,a):
    #rzadek liter t
    for i in range(n-1):
        litera_t(a)
        skok(2*a,4*a)
        rt(180)
        litera_t(a)
        rt(180)
        skok(-2*a,2*a)
    litera_t(a)
    skok(0,a)

        
def skok(a,b=0):
    pu()
    fd(a); rt(90)
    fd(b); lt(90)
    pd()

