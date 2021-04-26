"""
Problema físico 2: Dado o sistema abaixo onde m1 = 6kg e m2 = 4kg e o
coeficiente de atrito cinético é 0,2 entre o “bloco 1” e a prancha.
O bloco na prancha está encostado na mola de constante elástica 180N/m que está
inicialmente comprimida de 30cm. A mola é liberada empurrando o “bloco 1”,
sem afrouxar a corda. Ao final de 40cm de percurso qual a velocidade dos
blocos?
"""

print("* Primeiro passo: Definir as variáveis utilizadas no problema, e em "
      "seguida importar as bibliotecas para utilizar as funções requeridas. "
      "\n* Variáveis fornecidas no desafio. \n")

import math

m1 = 6  # massa 1 em quilograma
m2 = 4  # massa 2 em quilograma
Uc = 0.2  # coeficiente de atrito cinético
k = 180  # constante elástica
d = 0.4  # distancia final
x = 0.3  # distancia comprimida
g = 9.8  # gravidade

print("As variáveis definidas "
      "são:", m1, "-", m2, "-", Uc, "-", k, "-", d, "-", x, "-", g)

print("* Segundo passo: Realizar os cálculos básicos necessários para "
      "identificar a força na mola. \n")


def força(k, x):
    print("A força na mola comprimida é de:", ((-k) * x), "N. \n")


força(180, 0.3)
# F = (-k) * x
# print("A força na mola comprimida é de:", F,"N.")

print("* Terceiro passo: Calcular a energia inicial do sistema. \n")


# Obs: Para essa questão em específico, precisei efetuar a quebra de linha
# nas linhas 46 e 47 para ficar um código de acordo com a PEP 08.



def energia(k, x):
    print("A Energia Inicial do Sistema "
          "é de: Ei=", ((k * (x) ** 2) / 2),
          "J. Sistema em repouso inicialmente")


energia(180, 0.3)

# A resposta correta > Ei = 8.1J

"""
* Quarto passo: Calcular o restante do problema
"""


# Uc = Delta * Emec
# V1 = V2 = V
# Uc * m1 * d = Emec(final) - Emec(inicial)

# obs: Corda não afrouxa | d = h

# Uc * m1 * d = ((m2 * V2**2) / 2) + ((m1 * V1 * 2) / 2) - (m2 * g * d + Ei)

def atrito(Uc, m1, g, d):
    print("O coeficiente de atrito para essa equação é de: ", Uc * m1 * g * d,
          ".")


atrito(0.2, 6, 9.8, 0.4)

# Será feito o cálculo da variação da Energia mec utilizando uma lista com os
# valores das variáveis definidas no início do exercício

l = [6, 4, 9.8, 0.4, 8.1]  # lista contendo os valores das variáveis
resultado_parcial = ((l[1] / 2) + (l[0] / 2))
resultado_parcial1 = ((l[1] * l[2] * l[3]) + 8.1)
print(resultado_parcial, resultado_parcial1)

"""
* Quinto passo: No último passo do exercício, as equações serão igualadas para
se encontrar a resposta final, seerá realizado o cálculo
de radiciação utilizando a função "math".
"""

V_ao_quadrado = int(input("Digite o valor de V^2: "))
Delta_Emc = resultado_parcial1 + 4.78

if V_ao_quadrado == 5:
    print("O resultado final da velocidade é de: ",
          math.sqrt(Delta_Emc / V_ao_quadrado), "m/s")
else:
    print("O resultado está diferente do exercício.")


print("Eu quero ver se essa droga vai logar ou não agora no github")
