# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import wx

class Test(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title="Test")
		mainsz = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(mainsz)
		
		lc = wx.ListCtrl(self, -1, size=(-1,100),
                         style=wx.LC_REPORT
                         |wx.BORDER_SUNKEN)
		lc.InsertColumn(0, "C1")
		lc.InsertColumn(1, "C2")
		lc.InsertColumn(2, "C3")
		
		for x in range(0,5):
			lc.InsertStringItem(x, "RPY")
			lc.SetStringItem(x, 1, "HI")
			lc.SetStringItem(x, 2, "HI")
		
		mainsz.Add(lc, 1, wx.EXPAND)
		self.Centre(1)
		self.Show()

def main():
	app = wx.App()
	fr = Test(None)
	app.MainLoop()
	
if __name__=='__main__':
	main()
