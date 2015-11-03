# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import wx
import sympy
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from sympy import (sin,cos,tan,sec,csc,cot,ln,log,exp,asin,acos,atan,sqrt) # Algunas funciones
from cfg import *


def preproc(cad):
	"""
	Replace this function for other in "util" module
	"""
	return cad.replace("^","**")


class UIDer(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=PICHI_STR,size=(400,300))
		self.funpanel = wx.Panel(self,-1)
		
		self.initSizers()
		self.initCanvas()
		self.initCtrls()
		
		self.Centre(1)
		self.Show()
	
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.funsz = wx.BoxSizer(wx.HORIZONTAL)
		self.funpanel.SetSizer(self.funsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.funlabel = wx.StaticText(self.funpanel, -1, " f(x) ")
		self.fun = wx.TextCtrl(self.funpanel, -1, "")
		self.boton = wx.Button(self, -1, "Derivar")
		
		# Fonts
		font1 = self.funlabel.GetFont()
		font1.SetPointSize(12)
		self.funlabel.SetFont(font1)
		self.fun.SetFont(font1)
		self.fun.SetForegroundColour((0,0,255))
		
		self.funsz.Add(self.funlabel, 1, wx.EXPAND|wx.ALL, 5)
		self.funsz.Add(self.fun, 7, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.funpanel, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.boton, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.canvas, 6, wx.EXPAND|wx.ALL, 5)
		
		self.Bind(wx.EVT_BUTTON, self.derivar, self.boton)
		
	def initCanvas(self):
		self.figure = Figure()
		
		# FigureCanvas
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.figure.set_facecolor((1,1,1)) # ...
		self.string = self.figure.text(0.05, 0.5, "")
		self.string.set_fontsize(18)
		
	def derivar(self,event):
		x = sympy.Symbol("x")
		fx = self.fun.GetValue() # Función original
		fx = preproc(fx)
		Fx = sympy.diff(eval(fx)) # Función derivada
		str_Fx = "$\\frac{d}{dx}(%s)\, = \,%s$"%(sympy.latex(eval(fx)), sympy.latex(Fx))
		self.string.set_text(str_Fx)
		self.canvas.draw() # "Redibujar"



class UIInt(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=PICHI_STR,size=(400,300))
		self.funpanel = wx.Panel(self, -1)

		self.initSizers()
		self.initCanvas()
		self.initCtrls()
		
		self.SetBackgroundColour("#FFFFFF")
		
		self.Centre(1)
		self.Show()
	
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.funsz = wx.BoxSizer(wx.HORIZONTAL)
		
		self.funpanel.SetSizer(self.funsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.funlabel = wx.StaticText(self.funpanel, -1, " f(x) ")
		self.fun = wx.TextCtrl(self.funpanel, -1, "")
		self.boton = wx.Button(self, -1, "Integrar", size=(100,25))
		
		# Fonts
		font1 = self.funlabel.GetFont()
		font1.SetPointSize(12)
		self.funlabel.SetFont(font1)
		self.fun.SetFont(font1)
		self.fun.SetForegroundColour((0,0,255))
		
		self.funsz.Add(self.funlabel, 1, wx.EXPAND|wx.ALL, 5)
		self.funsz.Add(self.fun, 7, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.funpanel, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.canvas, 6, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.boton, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
		
		self.Bind(wx.EVT_BUTTON, self.integrar, self.boton)
		
	def initCanvas(self):
		self.figure = Figure()
		
		# FigureCanvas
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.figure.set_facecolor((1,1,1))
		self.string = self.figure.text(0.05, 0.5, "")
		self.string.set_fontsize(18)
		
	def integrar(self,event):
		x = sympy.Symbol("x")
		fx = self.fun.GetValue() # Función original
		fx = preproc(fx)
		Fx = sympy.integrate(eval(fx)) # Función integrada
		str_Fx = "$\int \, (%s) \,dx \,= \,%s + C$"%(sympy.latex(eval(fx)), sympy.latex(Fx))
		self.string.set_text(str_Fx)
		self.canvas.draw()
		


class UILimit(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=PICHI_STR,size=(400,300))
		self.funpanel = wx.Panel(self, -1)

		self.initSizers()
		self.initCanvas()
		self.initCtrls()
		
		self.Centre(1)
		self.Show()
	
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.funsz = wx.BoxSizer(wx.HORIZONTAL)
		
		self.funpanel.SetSizer(self.funsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.funlabel = wx.StaticText(self.funpanel, -1, " f(x) ")
		self.fun = wx.TextCtrl(self.funpanel, -1, "", style= wx.TE_PROCESS_ENTER)
		self.boton = wx.Button(self, -1, "Calcular limite")
		
		# Fonts
		font1 = self.funlabel.GetFont()
		font1.SetPointSize(12)
		self.funlabel.SetFont(font1)
		self.fun.SetFont(font1)
		self.fun.SetForegroundColour((0,0,255))
		
		self.funsz.Add(self.funlabel, 1, wx.EXPAND|wx.ALL, 5)
		self.funsz.Add(self.fun, 7, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.funpanel, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.boton, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.canvas, 6, wx.EXPAND|wx.ALL, 5)
		
		self.Bind(wx.EVT_BUTTON, self.limite, self.boton)
		self.Bind(wx.EVT_TEXT_ENTER, self.limite)
		
	def initCanvas(self):
		self.figure = Figure()
		
		# FigureCanvas
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.figure.set_facecolor((1,1,1))
		self.string = self.figure.text(0.05, 0.5, "")
		self.string.set_fontsize(18)
		
	def limite(self,event):
		x = sympy.Symbol("x")
		so = self.fun.GetValue() # Función original
		if not(so):
			print "Función no definida"
			return False
		so = preproc(so)
		so = so.split(",")
		fx = so[0]
		val = float(so[1])
		Fx = sympy.limit(eval(fx),x,val) # Función integrada
		str_Fx = r"$ \lim_{x \to %s} \, (%s) \,dx \,= \,%s$"%(val, sympy.latex(eval(fx)), sympy.latex(Fx))
		self.string.set_text(str_Fx)
		self.canvas.draw()
		
		
if __name__=='__main__':
	app = wx.App()
	fr = UILimit(None)
	app.MainLoop()
