"""
Aula algoritmos - ifes 21/01/2021 (Quinta-feira)

Atividade > Criar lista de planetas sistema solar

"""

sistema_solar = []

while True:
    planetas = input("Insira o nome dos planetas do sistema solar: ")

    if planetas == 'fim':
        break

    sistema_solar.append(planetas)

    print('************************************')
    print('     Sistema Solar     ')
    print('************************************')

    x = 0

    for p in sistema_solar:
        print('planetas ', x + 1, ' : ', p)
        x += 1

print(sistema_solar)