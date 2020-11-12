import turtle

def prepaint():
    #画框
    turtle.setup(512,512,512,0)
    turtle.color("tan")
    turtle.penup()
    turtle.speed(6)
    turtle.goto(-248,248)
    turtle.seth(0)
    turtle.begin_fill()
    turtle.circle(-490,90)
    turtle.seth(180)
    turtle.fd(490)
    turtle.seth(90)
    turtle.fd(490)
    turtle.end_fill()
    turtle.color("black")
    turtle.pensize(10)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(490)
    turtle.seth(0)
    turtle.fd(490)
    turtle.seth(90)
    turtle.fd(490)
    turtle.seth(180)
    turtle.fd(490)
    turtle.speed(512)
    #“Π”字样
    turtle.speed(4)
    turtle.penup()
    turtle.goto(-100,75)
    turtle.seth(0)
    turtle.pendown()
    turtle.fd(200)
    turtle.penup()
    turtle.goto(-35,75)
    turtle.pendown()
    turtle.seth(-110)
    turtle.fd(100)
    turtle.circle(-150,40)
    turtle.penup()
    turtle.goto(35,75)
    turtle.seth(-100)
    turtle.pendown()
    turtle.fd(80)
    turtle.speed(100)
    n=96
    for i in range(256):
        n-=0.4
        turtle.circle(n,3)

def paint(x,y,position):
    x,y=(x*496)-248,(y*496)-248
    if(bool(position)):
        turtle.color("darkorange")
    else:
        turtle.color("dimgray")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(10)