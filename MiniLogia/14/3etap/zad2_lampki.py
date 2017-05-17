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


def kwad(a):
    begin_fill()
    for i in range(4):
          fd(a);rt(90)
    end_fill()

def prost(wys,szer):
    begin_fill()
    for i in range(2):
          fd(wys);rt(90)
          fd(szer);rt(90)
    end_fill()

def swieczka(wys,szer):
    #swieczka
    color("black","orange")
    prost(wys,szer)
    
    #knot
    pu()
    fd(wys)
    rt(90)
    fd(szer/2)
    lt(90+45)
    color("black","red")
    pd()
    kwad(szer/sqrt(2))
    pu()
    rt(90+45)
    bk(szer/2)
    lt(90)
    bk(wys)
    pd()
  

def lampki(m):
  lt(90)
  n = m // 2
  sz = 720
  a = sz /(2 * n + 2)

  #podstawa
  pu(); bk(220);pd();rt(90)
  color("black","brown")
  begin_fill()
  for i in range(2):
      fd(sz/2);rt(90)
      fd(20);rt(90)
      fd(sz/2)
  pu();bk(sz/2+2*a);pd()
  end_fill()
  
  for i in range(n):
      pu();fd(2*a);pd()
      lt(90)
      swieczka(360-i*a,a)
      rt(90)

  pu();fd(5*a);pd()
  rt(180)
  for i in range(n):
      pu();fd(2*a);pd()
      rt(90)
      swieczka(360-i*a,a)
      lt(90)

 



