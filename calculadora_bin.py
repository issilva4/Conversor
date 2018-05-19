#coding: utf-8

binario = raw_input('Digite seu número binário: ')
list_binario = list(binario)	
binario_report = binario

if  '.' in binario :
	binario, pos_virgula = binario.split('.')
	cont = 1
	cont_potencia = 0
	for e in pos_virgula:
		e = float(e)
		potencia_frac = e/(2 * cont)
		cont_potencia += potencia_frac
		cont *=2
		
	potencia = 2**(len(binario)-1)
	num_dec = 0

	for i in binario:
		i = int(i)
		num_bit = i * potencia
		potencia /=2
		num_dec += num_bit
	num_dec +=cont_potencia
	print '%s(2) = %f(10)' % (binario_report,num_dec)


elif  ',' in binario :
	binario, pos_virgula = binario.split(',')
	cont = 1
	cont_potencia = 0
	for e in pos_virgula:
		e = float(e)
		potencia_frac = e/(2 * cont)
		cont_potencia += potencia_frac
		cont *=2
		
	potencia = 2**(len(binario)-1)
	num_dec = 0

	for i in binario:
		i = int(i)
		num_bit = i * potencia
		potencia /=2
		num_dec += num_bit
	num_dec +=cont_potencia
	print '%s(2) = %f(10)' % (binario_report,num_dec)
else :
	potencia = 2**(len(binario)-1)
	num_dec = 0

	for i in binario:
		i = int(i)
		num_bit = i * potencia
		potencia /=2
		num_dec += num_bit
	print '%s(2) = %s(10)' % (binario_report,num_dec)
print'\n========================\n========================\n         V 1.0        \n========================\n========================'
