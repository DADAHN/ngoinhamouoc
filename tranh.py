import turtle as t
#BỐI CẢNH
t.penup()
t.goto(-100,-200)
t.speed(6)
t.pendown()
t.pensize(4)
t.pencolor("black")
t.bgcolor("grey")


#NHÀ
t.fillcolor("blue")
t.begin_fill()
t.rt(90)
n=0
while n<2:
	t.rt(90)
	t.fd(150)
	t.rt(90)
	t.fd(160)
	n=n+1
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.lt(120)
t.fd(80)
t.lt(60)
t.fd(160)
t.lt(120)
t.fd(80)
t.end_fill()

t.fillcolor("violet")
t.begin_fill()
t.rt(90)
t.fd(150)
t.lt(120)
t.fd(150)
t.end_fill()
t.lt(180)
t.penup()
t.fd(150)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.rt(30)
t.fd(80)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(80)
t.end_fill()
t.penup()
t.goto(-50,-50)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.fd(30)
t.lt(60)
t.fd(30)
t.lt(120)
t.fd(30)
t.lt(60)
t.fd(30)
t.end_fill()

t.penup()
t.goto(-150,-200)
t.pendown()
t.fillcolor("green")
t.begin_fill()
i=0
while i<2:
	t.fd(80)
	t.lt(90)
	t.fd(50)
	t.lt(90)
	i=i+1
t.end_fill()



#CÂY
t.penup()
t.goto(200,-200)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
i=0
while i<2:
	t.fd(80)
	t.rt(90)
	t.fd(30)
	t.rt(90)
	i=i+1
t.end_fill()
t.penup()
t.goto(200,-120)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.lt(90)
t.fd(30)
i=0
while i<3:
	t.rt(120)
	t.fd(90)
	i=i+1
t.end_fill()

t.rt(120)
t.fd(90)
t.rt(60)
t.fillcolor("green")
t.begin_fill()
t.fd(45)
i=0
while i<3:
	t.lt(120)
	t.fd(90)
	i=i+1
t.end_fill()
t.lt(120)
t.fd(90)
t.lt(60)
t.fillcolor("green")
t.begin_fill()
t.fd(45)
i=0
while i<3:
	t.rt(120)
	t.fd(90)
	i=i+1
t.end_fill()



#MẶT TRỜI
t.penup()
t.goto(100,250)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.rt(90)
t.fd(50)
t.penup()
t.goto(100,150)
t.lt(180)
t.pendown()
t.fd(50)
t.penup()
t.goto(50,200)
t.pendown()
t.rt(90)
t.fd(50)
t.penup()
t.goto(150,200)
t.pendown()
t.lt(180)
t.fd(50)
t.penup()
t.goto(100,200)
t.lt(45)
t.fd(50)
t.pendown()
t.fd(30)
i=0
while i<3:
	t.penup()
	t.goto(100,200)
	t.lt(90)
	t.fd(50)
	t.pendown()
	t.fd(30)
	i=i+1


t.done()