#!/usr/bin/python

animais = ['tigra', 'boi', 'galinha']

def exibir_lista(lista):
	for a in lista:
		print a

exibir_lista(animais)

def somar(a, b):
	return a+b

resultado = somar(5, 2)

print resultado

###########################

def subtrair(*args):
 	print args

subtrair(2,3,10,50)

def multiplicar(*args,**kwargs):
	print kwargs
	print args

multiplicar(a=2,b=1,c=4,d=6)

############################

f = lambda x,y,z: x + y + z

print f(2,3,4)

############################

words = ['pera', 'uva', 'mamao']

frutas = lambda words: [len(w) for w in words]

print frutas(words)

###########################

try:
	print 'primeira linha'
	func()
	print 3  + 3

except Exception as e:

	print e

	print 'Algo de errado aconteceu'


def func2():
	pass

try:
	print 'primeira linha'
	func2()
	print 3 + 3

except Exception as e:

	print 'Algo de errado aconteceu'

#########################

def func3(valor):
	if valor:
		raise Expection('Deu ruim')

try:
	print 'primeira linha'
	func3(True)
	print 3 + 3

except Expection as e:
	print e
finally:
	print 'sempre executa'
