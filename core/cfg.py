# -*- coding: utf-8 -*-
# ***********************************
#  PiChi 0.0.1
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
VERSION = "0.0.1"
PICHI_STR = "PiChi "+VERSION+"  "


STATEMENTS = {
	"plot":"plot\([0-9A-Za-z /+\-\*\^\(\)]*\,\d*,\d*\)",
	"integrate":"integrate\([0-9A-Za-z /+\-\*\^]*\,\w\)",
	"derivative":"derivative\([0-9A-Za-z /+\-\*\^]*\,\w\)"
}
