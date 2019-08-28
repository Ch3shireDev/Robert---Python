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

#zadanie 1 miniLOGIA 14

def kwiat():
    #procedura główna, bok - zmienna pomocnicza
    bok = 8
    lt(90)
    for i in range(6):
        pu(); fd(19*bok); pd()
        platek(bok)
        pu(); bk(19*bok); pd()
        rt(60)
    #płatek w środku
    platek(bok)

def platek(bok):
    #płatki złożone z  sześciokątów
    for i in range(6):
        pu(); fd(bok); pd()
        szesciokat(4*bok)
        pu(); bk(bok); pd()
        rt(60)

def szesciokat(bok):
    #żółty sześciokąt
    fillcolor("yellow")
    begin_fill();
    fd(bok);lt(60)
    fd(bok);rt(120)
    fd(bok);rt(60)
    fd(bok);rt(60)
    fd(bok);rt(60)
    fd(bok);rt(120)
    end_fill();




