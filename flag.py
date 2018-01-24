import turtle 

def flag(t,t1):

	t.color('green')
	t1.color('orange')
	t.pencolor('black')
	t1.pencolor('black')
	t.begin_fill()
	t1.begin_fill()
	t.goto(300,-100)
	t1.goto(-300,100)
	t.goto(300,-300)
	t1.goto(-300,300)
	t.goto(-300,-300)
	t1.goto(300,300)
	t.goto(-300,-100)
	t1.goto(300,100)
	t.goto(0,-100)
	t1.goto(0,100)
	t.goto(-300,-100)
	t1.goto(300,100)
	t1.end_fill()
	t.end_fill()
	t.color('black')
	t1.color('black')
	t.left(90)
	t1.right(90)
	t.forward(100)
	t1.forward(100)
	#t2=turtle.Turtle()

def wheel(t):
	t.speed(8)
	for i in range(24):
		t.pensize(3)
		t.left(15)
		t.forward(70)
		t.left(90)
		t.forward(5)
		t.backward(10)
		t.forward(5)
		t.right(90)
		t.backward(70)

		t.stamp()

def base():
	#initialize
	t1=turtle.Turtle()
	t=turtle.Turtle()
	t1.speed(8)
	t.speed(8)
	#wheel
	t.color('blue')
	wheel(t)
	
	t1.pensize(3)
	t.color('black')
	t.up()
	t1.up()
	t.goto(0,-100)
	t1.goto(0,100)
	t.down()
	t1.down()

	#flag
	flag(t,t1)
	


base()
while True:
	pass