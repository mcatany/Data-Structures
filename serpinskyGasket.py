from turtle import *
color('red')

dim = 240;
minSize = 8;

def draw_gasket(dim):
		setposition(0,0)
		goto(200,0)
		goto(200,200)
		goto(0,200)
		goto(200,0)
		goto(0,0)
		goto(0,200)
		goto(0,0)
		pu()
		goto(100,100)
		pd()
		goto(200,200)

draw_gasket(dim)