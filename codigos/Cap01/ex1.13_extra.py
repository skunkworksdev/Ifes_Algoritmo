'''
Codigo de Wesley ....

'''

# v0 = 5 		#m/s
g = 9.8 	#m/s^2
# t = 0.6		# s
# y0 = 0		# m

y0 = float(input('Entre com a posição inicial: '))
v0 = float(input('Entre com a velocidade inicial: '))
t = float(input('Entre com o tempo final: '))

y = y0 + v0*t - (1/2)*g*t**2

print('A posição final é y(',t,') = ',y,' m ')
