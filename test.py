
dicionario = [{'caminhao':{'papito': 'agua'}}]

def adicionar_valor_interno_com_chave_usuario(lista, posicao):
    try:
        # Acessa o dicionário na posição especificada
        dicionario = lista[posicao]

        # Acessa o dicionário interno através da chave externa
        dicionario_interno = dicionario['caminhao']
        
        # Solicita ao usuário o nome da chave interna
        chave_interna = input("Insira o nome da chave interna: ")
        
        # Solicita ao usuário o novo valor
        novo_valor = input(f"Insira o valor para a chave '{chave_interna}': ")
        
        # Adiciona ou atualiza o valor na chave interna
        dicionario_interno[chave_interna] = novo_valor
        
        print(f"Valor da chave '{chave_interna}' alterado para '{novo_valor}' no dicionário {posicao+1} dentro de 'caminhao'.")
        print(dicionario)
        
    except IndexError:
        print(f"Não existe um dicionário na posição {posicao+1}.")

adicionar_valor_interno_com_chave_usuario(dicionario, 0)