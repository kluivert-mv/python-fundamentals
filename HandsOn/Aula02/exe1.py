#!/usr/bin/python

idade = int(raw_input("Qual sua idade: "))

estado = raw_input("Voce esta alcoolizado: sim ou nao").upper()

habilitado = raw_input("Voce e habilitado: sim ou nao").upper()


if idade >= 18 and estado == 'NAO' and habilitado == 'SIM':
	print "Voce pode dirigir!"
else:
	print "Voce nao pode dirigir!"

