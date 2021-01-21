import math

pi = math.pi

r = float(input("Entre com o raio do circulo em metros: "))

C = 2*pi*r

A = pi*r**2

#print("O comprimento da circunferência é: ",C," m")
#print("A área da circulo é: ",A," m^2")

print("O comprimento da circunferência é: %.3f m" %C)
print("A área da circulo é: : %.3f m^2" %A)