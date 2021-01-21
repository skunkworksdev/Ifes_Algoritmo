dC = 5; C0 = -20; Cf = 40
C = C0
lista_Celsius = []; lista_Fahren = []

while C < Cf:
	lista_Celsius.append(C)
	F = (9.0/5)*C + 32
	lista_Fahren.append(F)
	C = C + dC
	print('%5.2f %5.2f' % (C, F))

