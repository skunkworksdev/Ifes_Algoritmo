lista_C = list(range(-20,45,5))

n = len(lista_C)

lista_F = [0.0]*n	#lista vazia

for i in range(n):
	lista_F[i] = (9/5)*lista_C[i] + 32
	print(" %3.4f   |   %3.4f " %(lista_C[i],lista_F[i]))
	
	
print('********')	
print('n = ',n)	
print('********')	
print('lista Celsius = ',lista_C)
print('********')	
print('lista Fahrenheit = ',lista_F)