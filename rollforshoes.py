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

import os
import time
import random

dado = 0
dado_contrario = 0

while True:
    ato = int(input('Insira 1 para rodar e 2 para sair: '))

    if ato == 1:
        print('Jogador [nome do jogador]')
        #habilidades são variáveis de jogador para jogador
        print('1 - Fazer alguma coisa [1]')
        opcao = int(input('Selecione sua habilidade: '))

        print('\n')

        print('GM [nome do GM]')
        print('1 - Fácil')
        print('2 - Normal')
        print('3 - Difícil')
        print('4 - Praticamente impossível')
        dificuldade = int(input('Selecione a dificuldade da ação: '))

        if opcao == 1:
            # for x in range(nivel):
            #     dado += (random.randint(1,6))

            dado += (random.randint(1,6))

            for x in range(dificuldade):
                dado_contrario += (random.randint(1,6))

            if dado > dado_contrario:
                print(f'Ação bem sucedida! Seu dado foi {dado}, em relação ao {dado_contrario} do dado contrário.')
                time.sleep(2)
                os.system("cls")
            elif dado == dado_contrario:
                print(f'Empate! Seu dado foi {dado}, em relação ao {dado_contrario} do dado contrário.')
                time.sleep(2)
                os.system("cls")
            else:
                print(f'Você falhou! Seu dado foi {dado}, em relação ao {dado_contrario} do dado contrário.')
                time.sleep(2)
                os.system("cls")
                #+1 Experiência
    elif ato == 2:
        break
    else:
        print('[ERRO] Opção Inválida!')


    

    
