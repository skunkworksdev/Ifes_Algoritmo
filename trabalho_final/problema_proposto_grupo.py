"""
Problema físico proposto pelo grupo: Na figura abaixo uma bola maciça de massa
0,28g rola suavemente ao longo do trilho quando é liberada a partir do repouso.
O círculo tem raio R = 14 cm e a bola tem raio r, muito menor que R.
a) Encontre a altura h para que a bola perca o contato com o trilho no ponto
mais alto do circulo.
b) Se agora h = 6R, encontre o vetor força que o trilho faz sobre a bola no
ponto Q?
"""

print("* Primeiro passo: Definir as variáveis utilizadas no problema, "
      "e em seguida importar as bibliotecas para utilizar as funções "
      "requeridas. \n* Variáveis fornecidas no desafio")

m = 0.00028
R = 0.14
g = 9.8


# Letra A: Encontre a altura h para que a bola perca o contato com o trilho
# no ponto mais alto do circulo.

h = (((20 * R * g) + (7 * R * g)) / (10 * g))
if h == 0.37800000000000006:
    print("A altura (h) para que a bola perca o contato "
          "direto com o trilho é de:", h)
else:
    print("Por favor, recalcue seus dados.")


# Letra B: Se agora h = 6R, encontre o vetor força que o trilho faz sobre
# a bola no ponto Q?

def equacao(m, R, g):
    N = m * (((50 * R * g) / 7) / R)
    print("\nPara o ponto Q, o vetor força que o trilho "
          "fazo sobre a bola é de:", N)


equacao(0.00028, 0.14, 9.8)
