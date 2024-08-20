# REGRAS DO JOGO

# 1. Say what you do and roll a number of D6s, determined by the level of relevant skill you have.

# 2. If the sum of your roll is higher than an opposing roll, the thing you wanted to happen, happens.

# 2. At start, you have only one skill: Do Anything 1.

# 4. If you roll all 6s, you get a new skill specific to the action, one level higher than the one you used.

# 5. For every roll you fail, you get 1 XP.

# 6. XP can be used to change a die into a 6 for advancement purposes only.

# 7. When your result is a tie with the opposing roll, you both partially succeed and fail. 
# You don't get XP, and accomplish your goal barely with an unexpected twist.

# 8. When opposition is not from another character, the GM rolls a number of dice based on how difficult a task is:
# 1 - Easy / 2 - Average / 2 - Hard / 4 - Nearly impossible

# FUNÇÕES
# - Rolar os dados (tanto seu como o oposto de acordo com a dificuldade)
# - Inserir seus jogadores e dados (exp e habilidades)
# - SIstema de Expêriência
# - Definir dificuldade da ação GM
# - Opção de normal play ou batalha
# - Em modo batalha os dados são rolados para definir a ordem de cada um irá atacar.

import os
import time
import random

jogadores = []

def mostrar_jogadores():
    print('\n')
    print(f'--> Aventureiros da mesa de {DM} <---')
    for x in jogadores: 
            counter = 0
            print(f"[Ficha de {x['Nome']}]")
            print(f"XP: {x['Experiencia']}")
            print('Habilidades:')
            for y in x['Habilidades']:
                for chave,valor in y.items():
                    counter += 1
                    print(f'{counter}. {chave} [{valor}]')
            print('\n')

print('o---SUPER ROLL FOR SHOES---o')
print('[1] Iniciar uma nova aventura!')
print('[2] SAIR.')

ato = int(input('Insira o número correspondente a ação que deseja fazer: '))

os.system("cls")

if ato == 1:
    print('o---SUPER ROLL FOR SHOES---o')
    print('\n')
    DM = input(f'Insira o nome do Dungeon Master: ')
    print('\n')
    quant_jogadores = int(input('Insira a quantidade de jogadores: '))
    print('\n')
    for x in range(quant_jogadores):
        nome = input(f'Insira o nome do jogador {x+1}: ')
        jogador = {'Nome': nome,'Experiencia': 0,'Habilidades': [{'Fazer alguma coisa': 1}]}
        jogadores.append(jogador)

    while True:
        os.system("cls")
        print(f'--> Mesa de {DM} em andamento... <---')
        print('[1] Rolar os dados.')
        print('[2] Mostrar fichas')
        print('[3] Encerrar Aventura.')

        ato = int(input('Insira o número correspondente a ação que deseja fazer: '))

        if ato == 1:
            ficha = 0

            os.system("cls")
            mostrar_jogadores()
            rolador = input('Insira o nome do jogador que irá rolar: ')
            for x in jogadores:
                while True:
                    if rolador == x['Nome']:
                        ficha = x                     
                        break
                    else:
                        os.system("cls")
                        mostrar_jogadores()
                        print('[ERRO] Nome de jogador inválido.')
                        rolador = input('Insira o nome do jogador presente na mesa que irá rolar: ')

            print('\n')

            counter = 0
            print(f"[Habilidades de {ficha['Nome']}]")
            for y in ficha['Habilidades']:
                for chave,valor in y.items():
                    counter += 1
                    print(f'{counter}. {chave} [{valor}]')

            print('\n')

            num_habilidade = int(input('Digite o número correspondente a habilidade: '))
            posicao_interna = ficha['Habilidades']
            habilidade_escolhida = posicao_interna[num_habilidade-1]
            lista_habilidade = list(habilidade_escolhida)
            chave_habilidade = lista_habilidade[0]
            dado_habilidade = habilidade_escolhida[chave_habilidade]

            print(dado_habilidade)
            
            menu = input('Aperte qualquer tecla para voltar para o menu.')

        elif ato == 2:
            mostrar_jogadores() 
            menu = input('Aperte qualquer tecla para voltar para o menu.')
    