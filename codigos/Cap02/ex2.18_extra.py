n = int(input('Entre com o primeiro valor a ser contado '))
m = int(input('Entre com o segundo valor a ser contado '))

print('----------------------------------------- ----------')

i = 0
di = 0.0000001
dj = 0.0000001
while i < n:
	i = i + di
	j = 0 		# temos q zerar o j para cada identação de i
	while j < m:
		j = j + dj
		print(i,j)

