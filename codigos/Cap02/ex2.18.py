n = int(input('Entre com o primeiro valor a ser contado '))
m = int(input('Entre com o segundo valor a ser contado '))

print('----------------------------------------- ----------')

i = 0
while i < n:
	i = i + 1
	j = 0 		# temos q zerar o j para cada identação de i
	while j < m:
		j = j + 1
		print(i,j)


# se não zerar o j após a primeira iteração, ele só faz uma iteração em j.

print('-------- se não zerar o j a cada iteração ----------')
i = 0
j = 0 
while i < n:
	i = i + 1
	while j < m:
		j = j + 1
		print(i,j)
