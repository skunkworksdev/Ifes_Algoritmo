lista_C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
lista_F = []	#lista vazia

for TC in lista_C:
	TF = (9/5)*TC + 32
	lista_F.append(TF)
	print(" %3.4f   |   %3.4f " %(TC,TF))
	
	
print('********')	
print(lista_F)