# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import wx
from cfg import *

class Derivar(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=PYXMATH_NAME,size=(400,300))
		self.Centre(1)
		self.Show()
	
class Integrar(wx.Frame):
	pass
	

if __name__=='__main__':
	app = wx.App()
	fr = Derivar(None)
	app.MainLoop()
