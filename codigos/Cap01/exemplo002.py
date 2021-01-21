#==============================================
#Exemplo 002
# Codigo de Wesley
#
#==============================================

x = int(input("Entrar com o primeiro número: "))
# o comando int converte string em inteiro

y = int(input("Entrar com o segundo número: "))

soma = x + y		#operação de soma		
sub = x-y
mult = x*y
divisao = x/y

div_int = x//y		#divisão inteira 10/6 = 1+4/6
resto = x%y			#resto da divisão

print("a soma de ",x," + ",y," = ",soma)
print("a subtração ",x," - ",y," = ",sub)
print("a multiplicação ",x," * ",y," = ",mult)
print("a divisão ",x," / ",y," = ",divisao,"e a inteira",int(divisao))
print("a divisão inteira é: ",div_int)
print("o resto da divisão é: ",resto)