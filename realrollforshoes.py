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

def rolar_dado(quant_dado):
    dado = 0
    for x in range(quant_dado):
        dado += (random.randint(1,6))
        return dado
    
def criar_jogador():
    global jogadores
    print('\n')
    nome = input(f'Insira o nome do jogador {x+1}: ')
    jogador = {'Nome': nome,'Experiencia': 0,'Habilidades': [{'Fazer alguma coisa': 1}]}
    jogadores.append(jogador)

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

while True:
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
        for x in range(quant_jogadores):
            criar_jogador()

        while True:
            os.system("cls")
            print(f'--> Mesa de {DM} em andamento... <---')
            print('[1] Rolar os dados.')
            print('[2] Mostrar fichas.')
            print('[3] Adicionar Jogadores.')
            print('[4] Encerrar Aventura.')

            ato = int(input('Insira o número correspondente a ação que deseja fazer: '))

            if ato == 1:
                ficha = 0
                jogador_existe = False
                os.system("cls")
                print('[o-- ROLAR OS DADOS... --o]')
                mostrar_jogadores()
                rolador = input('Insira o nome do jogador que irá rolar: ')
                for x in jogadores:
                        if rolador == x['Nome']:
                            jogador_existe = True
                            ficha = x 
                
                if jogador_existe == False:
                        while jogador_existe == False:
                            os.system("cls")
                            print('[o-- ROLAR OS DADOS... --o]')
                            mostrar_jogadores()
                            print('[ERRO] Nome de jogador inválido.')
                            rolador = input('Insira o nome do jogador presente na mesa que irá rolar: ')
                            for x in jogadores:
                                if rolador == x['Nome']:
                                    jogador_existe = True
                                    ficha = x 
                                    
                os.system("cls")
                counter = 0
                print(f"[Habilidades de {ficha['Nome']}]")
                for y in ficha['Habilidades']:
                    for chave,valor in y.items():
                        counter += 1
                        print(f'[{counter}] {chave} | Nível = {valor}')

                print('\n')

                num_habilidade = int(input('Digite o número correspondente a habilidade: '))
                
                #
                habilidades = ficha['Habilidades']
                habilidade_escolhida = habilidades[num_habilidade-1]
                lista_habilidade = list(habilidade_escolhida)
                chave_habilidade = lista_habilidade[0]
                nivel_habilidade = habilidade_escolhida[chave_habilidade]

                dado_jogador = rolar_dado(nivel_habilidade)

                print('\n')

                print(f'[Dungeon Master {DM}]')
                print('1 - Fácil')
                print('2 - Normal')
                print('3 - Difícil')
                print('4 - Praticamente impossível')
                dificuldade = int(input('Selecione o nível de dificuldade da ação: '))

                dado_dm = rolar_dado(dificuldade)
                print('\n')
                if dado_jogador > dado_dm:
                    print(f'Ação bem sucedida! Seu dado foi {dado_jogador}, em relação ao {dado_dm} do dado contrário.')
                elif dado_jogador == dado_dm:
                    print(f'Empate! Seu dado foi {dado_jogador}, em relação ao {dado_dm} do dado contrário.')
                elif dado_jogador == 6 and nivel_habilidade == 1:
                    pass
                    #nova habilidade
                else:
                    print(f'Você falhou! Seu dado foi {dado_jogador}, em relação ao {dado_dm} do dado contrário.')
                
                print('\n')
                input('Aperte qualquer tecla para voltar para o menu.')

            elif ato == 2:
                os.system('cls')
                print('[o-- MOSTRAR FICHAS --o]')
                mostrar_jogadores() 
                input('Aperte qualquer tecla para voltar para o menu.')

            elif ato == 3:
                os.system('cls')
                print('[o-- ADICIONAR JOGADORES --o]')

                criar_jogador()

            elif ato == 4:
                print('\n')
                print('Até a próxima aventura!')
                time.sleep(3)
                os.system('cls')
                break 
    
    elif ato == 2: 
        print('See you traveler...')
        time.sleep(3)
        break

