"""
Created on Wed Feb 24 14:27:34 2021

@author: luizm
"""

idade_pessoas = {
    'Ana': 7,
    'José': 38,
    'Paulo': 22,
    'Lucia': 59,
    'Cristina': 44,
    'Luiz': 12
}

maiores_de_idade = []
menores_de_idade = []

while len(idade_pessoas) >= 0:
    pessoas = list(idade_pessoas.keys())
    pessoa = pessoas[0]

    if idade_pessoas[pessoa] >= 18:
        maiores_de_idade.append(pessoa)
    else:
        menores_de_idade.append(pessoa)

    del idade_pessoas[pessoa]