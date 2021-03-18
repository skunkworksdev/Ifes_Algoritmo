"""
Problema físico 3: Na figura abaixo, uma polia feita de um cilindro maciço
tem 20cm de raio, montada em um eixo horizontal sem atrito. O momento de
inércia de um cilindro maciço é 1/2 MR. Uma corda de massa desprezível é
enrolada a polia e presa a uma caixa de 2,0kg que escorrega sob um plano
inclinado de 20º com a horizontal cujo atrito tem coeficiente 0,1.
Se ele desce com uma aceleração de 2m/s2, qual será a massa da polia?
"""

print("* Primeiro passo: Definir as variáveis utilizadas no problema, "
      "e em seguida importar as bibliotecas para utilizar as funções "
      "requeridas. \n* Variáveis fornecidas no desafio")



#%%

import math


vetor = [0.20, 0.5, 2, 0.349, 0.1, 2, 9.8]

# r = 0.20 - raio do cilindro - 0
# i = 0.5 - momento de inércia de um cilindro maciço - 1
# massa1 = 2 - massa da caixa - 2
# angulo_theta = 0.349 - ângulo do declive - 3
# u = 0.1 - coeficiente de atrito - 4
# a = 2 - aceleração - 5
# g = 9.8 - gravidade - 6

print("\n* Segundo passo: Realizar os cálcuos inicias básicos.")


Py = math.cos(vetor[3]) * vetor[2] * vetor[6]
Px = vetor[2] * vetor[6] * math.sin(vetor[3])
Fat = 0.1 * Py
print(Py)
print(Px)
print(Fat)


# T = M * a / 2 > Fórmula para cálculo da tração.
# T = M * 2 / 2 > T = M

print("\n* Terceiro passo: Calcular força resultante")


# T = Px - Fat - (m * a)
def massa_polia(Px, Fat, m, a):
    if (m * a) == 4:
        print("O resultado final da massa da polia é "
              "de: ", Px - Fat - (m * a),"Kg.")
    else:
        print("O resultado está errado, por favor, reveja os "
              "dados das variáveis.")

massa_polia(6.702381963625423, 1.8418416761862806, 2, 2)


