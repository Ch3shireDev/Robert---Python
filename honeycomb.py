from turtle import *

a = 40
posx,posy = [],[]


def hex():
    global a
    global posx,posy
    penup()
    fd(a)
    rt(120)
    pendown()
    for _ in range(6):
        fd(a)
        x,y=pos()
        posx += [x]
        posy += [y]
        rt(60)
    penup()
    lt(120)
    fd(-a)
    
def adj(t):
    global a
    rt(t*60)
    fd(a)
    rt(60)
    fd(a)
    lt(60+t*60)

speed(0)
tracer(0,0)

lt(90)

t = 0

for i in range(20):
    hex()
    if i<10:
        if i%3:
            t+=1
        else: 
            t-=1
    else:
        if i%3:
            t-=1
        else:
            t+=1

    adj(t)
    hex()

print(min(posx),max(posx))
L = max(posx)-min(posx)

print(a/L)

done()