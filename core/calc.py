# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import sympy
from sympy import (sin,cos,tan,exp,log)

def derivative(args):
	f = args[0]
	var = args[1]
	df = sympy.diff(f,var)
	return df
	
def integrate(args):
	f = args[0]
	var = args[1]
	exec ("var = sympy.Symbol('%s')"%(var))
	fi = sympy.integrate(f,var)
	return fi
