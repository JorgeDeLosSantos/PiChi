# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Jorge De Los Santos     
#  Email: delossantosmfq@gmail.com 
#  License: BSD License            
# ***********************************
import wx
from core import uicalc
from core.uicon import Console

class PiChi(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title="PiChi  0.0.1", size=(800,600))
		#style = wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX))
		self.initSizers()
		self.initCtrls()
		self.initMenu()
		
		self.Maximize(1)
		self.Centre(1)
		self.Show()
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.cli = Console(self)
		self.mainsz.Add(self.cli, 1, wx.EXPAND|wx.ALL, 5)
	
	def initMenu(self):
		marchivo=wx.Menu()
		abrir=marchivo.Append(-1, "Abrir\tCtrl-O")
		guardar=marchivo.Append(-1, "Guardar\tCtrl-S")
		guardarComo=marchivo.Append(-1, "Guardar como")
		
		mconfigurar=wx.Menu()
		ctema=mconfigurar.Append(-1, "Configurar tema")
		
		mayuda=wx.Menu()
		ayuda=mayuda.Append(-1, "Ayuda")
		acerca=mayuda.Append(-1, "Acerca de...")
		
		#Menú Álgebra
		malgebra = wx.Menu()
		_reseq = malgebra.Append(-1, u"Resolver ecuación")
		_ressiseq = malgebra.Append(-1, "Resolver sistema de ecuaciones lineales")
		_simp = malgebra.Append(-1, u"Simplificar expresión")
		_fact = malgebra.Append(-1, u"Factorizar expresión")
		_expand = malgebra.Append(-1, u"Expandir expresión")
		
		# Menú Cálculo
		mcalculo = wx.Menu()
		_derivar = mcalculo.Append(-1, "Derivar")
		_integrar = mcalculo.Append(-1, "Integrar")
		_limites = mcalculo.Append(-1, u"Límites")
		
		# Menú Álgebra Lineal
		malglin = wx.Menu()
		_det = malglin.Append(-1, "Determinante")
		_inv = malglin.Append(-1, "Matriz inversa")
		_trans = malglin.Append(-1, u"Transpuesta")
		
		# Meńu Gráficas
		mgraficas = wx.Menu()
		_2D = mgraficas.Append(-1, "f(x)")
		_3D = mgraficas.Append(-1, "f(x,y)")
		
		self.barraMenu=wx.MenuBar()
		self.barraMenu.Append(marchivo, "Archivo")
		self.barraMenu.Append(malgebra, u"Álgebra")
		self.barraMenu.Append(mcalculo, u"Cálculo")
		self.barraMenu.Append(malglin, u"Álgebra Lineal")
		self.barraMenu.Append(mgraficas, u"Gráficas")
		self.barraMenu.Append(mconfigurar, "Configurar")
		self.barraMenu.Append(mayuda, "Ayuda")
		self.SetMenuBar(self.barraMenu)
		
		self.Bind(wx.EVT_MENU, self.call_ui, _reseq)
		self.Bind(wx.EVT_MENU, self.call_ui, _ressiseq)
		self.Bind(wx.EVT_MENU, self.call_ui, _simp)
		self.Bind(wx.EVT_MENU, self.call_ui, _fact)
		self.Bind(wx.EVT_MENU, self.call_ui, _expand)
		self.Bind(wx.EVT_MENU, self.call_ui, _derivar)
		self.Bind(wx.EVT_MENU, self.call_ui, _integrar)
		self.Bind(wx.EVT_MENU, self.call_ui, _limites)
		self.Bind(wx.EVT_MENU, self.call_ui, _det)
		self.Bind(wx.EVT_MENU, self.call_ui, _inv)
		self.Bind(wx.EVT_MENU, self.call_ui, _trans)
		self.Bind(wx.EVT_MENU, self.call_ui, _2D)
		self.Bind(wx.EVT_MENU, self.call_ui, _3D)
	
	def call_ui(self,event):
		opt_str = self.barraMenu.FindItemById(event.GetId()).GetText()
		go_to = {
			u"Resolver ecuación":"",
			u"Resolver sistema de ecuaciones lineales":"",
			u"Simplificar expresión":"",
			u"Factorizar expresión":"",
			u"Expandir expresión":"",
			u"Derivar":"uicalc.UIDer(None)",
			u"Integrar":"uicalc.UIInt(None)",
			u"Límites":"uicalc.UILimit(None)",
			u"Determinante":"",
			u"Matriz inversa":"",
			u"Transpuesta":"",
			u"f(x)":"",
			u"f(x,y)":""
		}
		if go_to.has_key(opt_str):
			eval(go_to.get(opt_str))	

	
def main():
	app = wx.App(False)
	fr = PiChi(None)
	app.MainLoop()

if __name__=='__main__':
	main()
