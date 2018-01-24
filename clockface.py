import turtle
def clock():
	t=turtle.Turtle()
	for i in range(12):
		t.left(30)
		t.forward(100)
		t.stamp()
		t.backward(100)
		t.stamp()
	t.goto(0,-100)

	while True:
		#t.fillcolor('red')
		t.left(1)
		t.forward(1.8)
			
		
print clock()
while True:
	pass
