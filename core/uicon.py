# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import wx
import evalin
import re

class Console(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,-1)
		self.txthist = []
		self.initSizers()
		self.initCtrls()
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.inputc = wx.TextCtrl(self, -1, "", size=(-1,30), style= wx.TE_PROCESS_ENTER)
		self.historyc = wx.TextCtrl(self, -1, "", style= wx.TE_READONLY|wx.TE_MULTILINE)
		self.workspace = Workspace(self)
		
		self.mainsz.Add(self.inputc, 0, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.historyc, 5, wx.EXPAND|wx.ALL, 10)
		self.mainsz.Add(self.workspace, 1, wx.EXPAND|wx.ALL, 10)
		
		self.Bind(wx.EVT_TEXT_ENTER, self.OnExecute)
		
	def OnExecute(self,event):
		instr = self.inputc.GetValue()
		self.inputc.SetValue("")
		res, ws = evalin.evalin(instr)
		this_str = instr + "\n\t\t\t" + unicode(res)
		self.txthist.append(this_str)
		global_str = "\n".join(self.txthist)
		self.historyc.SetValue(global_str)
		self.workspace.update(ws)
		

class Workspace(wx.ListCtrl):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
		
		self.InsertColumn(0, "Nombre", width=100)
		self.InsertColumn(1, "Valor", width=150)
		self.InsertColumn(2, "Tipo", width=150)
		
	def update(self,ws):
		self.DeleteAllItems()
		ws = self.non_native_vars(ws)
		for k,var in enumerate(ws.keys()):
			self.InsertStringItem(k, unicode(var))
			self.SetStringItem(k, 1, unicode(ws.get(var)))
			self.SetStringItem(k, 2, self.get_var_type(ws.get(var)))
			
	def non_native_vars(self,ws):
		tws = dict()
		for var in ws.keys():
			if not bool(re.findall("__\w*__",var)):
				tws[var] = ws.get(var)
		return tws
				
	def get_var_type(self,var):
		_vartype = unicode(type(var))
		vartype = re.findall("\'\w*\'", _vartype)
		vartype = ("".join(vartype)).replace("'","")
		return vartype

if __name__=='__main__':
	app = wx.App()
	fr = wx.Frame(parent=None, title="Test",size=(400,300))
	c = Console(fr)
	fr.Centre(1)
	fr.Show()
	app.MainLoop()
