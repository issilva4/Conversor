#coding: utf-8
restos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

def convertb(inteiro, base):
	nabase = []
	while inteiro > 0:
		nabase.append(restos[inteiro%base])
		inteiro /= base
		
	if len(nabase) == 0:
		nabase.append(0)
	
	nabase.reverse()
	
	return nabase
	
def convertbfrac(fracionario, base):
	nabase = []
	while fracionario != 0:
		fracionario *= base
		nabase.append(restos[int(fracionario)])
		fracionario -= int(fracionario)
	
	if len(nabase) == 0:
		nabase = [0]*50
	
	return nabase

def dec_to_fracionario(decimal, base):
	
	if decimal.find(",") >= 0:
		pint, pfrac = decimal.split(",")
		pint = convertb(int(pint), base)
		pfrac = convertbfrac(int(pfrac)*1.0/(10**len(pfrac)) + 0, base)
		
		aux = pint + [","] + pfrac
	else:
		aux = convertb(int(decimal), base)
	
	s = ""
	for x in aux:
		s += str(x)
	
	return s
