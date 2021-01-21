dC = 5
C0 = -20
n = 13

lista_Celsius = [0.0]*n
lista_Fahren = [0.0]*n

for i in range(n):
	lista_Celsius[i] = C0 + i*dC
	lista_Fahren[i] = (9.0/5)*lista_Celsius[i] + 32
	print('%5.2f %5.2f' % (lista_Celsius[i], lista_Fahren[i]))
