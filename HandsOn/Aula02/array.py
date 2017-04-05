#!/usr/bin/python

animais = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais

animais.insert(1, 'tigre')
print animais

animais.remove('gato')
print animais

animais.pop()
print animais

print animais.count('tigre')
print animais

print animais.reverse()
print animais

###############################

matriz = [
	["python","php","go","nodesjs"],
	[1,2,3,4],

	]

print matriz[0][1]
print matriz[1][2]

