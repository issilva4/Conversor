#coding: utf-8
from dectofrac import *

print "CONVERSOR DECIMAL FRACIONÁRIO POSITIVO PARA BINÁRIO, OCTAL E HEXADECIMAL FRACIONÁRIO"
print "Para encerrar o programa, digite -1"

while True:
	decimal = raw_input("Insira o número decimal a ser convertido, separado por vírgula: ")
	
	if(decimal == "-1"):
		break
	
	print "\n------------------------------------------------------------------------------"
	print "Seu número em binário:", dec_to_fracionario(decimal, 2)
	print "Seu número em octal:", dec_to_fracionario(decimal, 8)
	print "Seu número em hexadecimal:", dec_to_fracionario(decimal, 16)
	print "------------------------------------------------------------------------------\n"
