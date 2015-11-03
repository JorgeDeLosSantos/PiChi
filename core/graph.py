# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,tan,log,exp

def plot(args):
	if len(args)==3:
		f = args[0]
		a = float(args[1])
		b = float(args[2])
	else:
		raise SyntaxError
	fig = plt.figure()
	ax = fig.add_subplot(111)
	x = np.linspace(a,b)
	y = eval(f)
	ax.plot(x,y)
	plt.show()

def plot3(args):
	print "Plot3Fun OnRev"
	pass

def surface(args):
	print "SurfaceFun OnRev"
	pass
	
if __name__=='__main__':
	plot(["x+sin(x)",0,10])
