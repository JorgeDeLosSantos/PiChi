# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import re
import graph
import calc
from cfg import *
import __ws
ws = __ws.__dict__.copy()

def evalin(instr):
	assign_case = re.findall("\w=\w",instr)
	if bool(assign_case):
		exec instr in ws
		return "",ws
	try:
		res = eval(instr, ws)
	except NameError:
		try:
			for fun in STATEMENTS.keys():
				isfun = re.findall(STATEMENTS.get(fun), instr)
				print isfun
				if bool(isfun):
					thisr = callfun(instr,fun)
					return thisr,ws
			raise SyntaxError
		except SyntaxError:
			res = u"Not assigned"
	return res,ws


def callfun(instr,fun):
	args = get_args(instr)
	#print "T", instr, fun
	LSF = {
		"plot":"graph.plot(args)",
		"integrate":"calc.integrate(args)",
		"derivative":"calc.derivative(args)"
	}
	hObj = eval(LSF.get(fun))
	return hObj


def get_args(instr):
	pat1 = "\w*\("
	pat2 = "\)\B"
	mod_instr = re.sub(pat1,"",instr)
	mod_instr = re.sub(pat2,"",mod_instr)
	args = mod_instr.split(",")
	print args
	return args
	
if __name__=='__main__':
	print get_args("plot(x,0,10)")
