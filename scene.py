import turtle
def sunlines(t):
	for i in range(12):
		t.color('yellow')
		t.left(30)
		t.penup()
		t.forward(100)
		t.pendown()

		t.forward(20)
		t.stamp()
		t.penup()
		t.backward(120)
	t.color('red')
	
def Scene():
	(t1,t2,t3)=(turtle.Turtle(),turtle.Turtle(),turtle.Turtle())
	t1.color('green')
	t2.color('green')
	t1.forward(480)
	t2.backward(480)
	t2.left(90)
	t1.left(90)
	t1.forward(50)
	t2.forward(50)
	t2.goto(-240,250)
	t1.goto(240,250)
	t2.goto(0,100)
	t1.goto(0,100)
	t1.color('black')
	#sun
	t3.penup()
	t3.left(90)
	t3.forward(275)
	t3.right(90)
	t3.forward(100)
	t3.pendown()
	
	sunlines(t3)
	t3.penup()
	t3.forward(80)
	t3.left(90)
	t3.pendown()
	
	for i in range(1000):
		#t.fillcolor('red')
		t3.left(1)
		t3.forward(1.5-(0.001)*i)
Scene()

while True:
	pass