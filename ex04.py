#Exercício 4 - Banco de Dados em dicionário
"""
Nesse exercício, o programa inicia criando um dicionário que armazena os inputs de usuário e já invoca a função de cadastrar os campos que popularão o dicionário como chave.
Logo após isso, o programa vai para seu loop principal, onde é permitido cadastrar um novo usuário (usando seus dados como valores da chave do dicionário) ou impressão dos usuários.
Se optar por imprimir os usuários, é aberto mais um switch case com as opções de impressão, sendo para imprimir todos ou de forma filtrada, estas opções funcionam percorrendo os values salvos.
Além disso, há a opção de digitar 0 no loop principal para encerramento do programa.
"""
#Criando o dicionário do banco de usuários
banco_usuarios = {}

#Função inicial para cadastrars usuário
def cadastrar_usuario(campos_obrigatorios):
    """ 
    Nesta função, é sugerido para o usuário digitar os valores que serão usados no dicionário criado com as chaves definidas anteriormente, se o usuário digitar sair,  a criação de usuário é finalizada.
    """
    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    while True:
        campo_extra = input("Digite um campo extra ou 'sair' para encerrar: ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Digite o valor para o campo '{campo_extra}': ")
        usuario[campo_extra] = valor_extra
    nome = usuario["nome"]
    banco_usuarios[nome] = usuario
    print("Usuário cadastrado com sucesso!")

#Função para imprimir usuários
def imprimir_usuarios(*args, **kwargs):
    """
    Aqui foi utilizado *args e **kwargs para fazer uma espécie de switch case que percorre o banco de usuários conforme as opções de impressão de usuário pedidas no enunciado.
    Se o input for 1, todos os usuários são impressos, 2 para impressão filtrando nomes, 3 para impressão filtrando campos e 4 filtrando nomes e campoos.
    """
    opcao = int(input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nDigite a opção: "))
    
    if opcao == 1:
        for nome, usuario in banco_usuarios.items():
            print(f"Nome: {nome}, Dados: {usuario}")
    elif opcao == 2:
        nomes = input("Digite os nomes separados por vírgula: ").split(", ")
        for nome in nomes:
            if nome in banco_usuarios:
                print(f"Nome: {nome}, Dados: {banco_usuarios[nome]}")
    elif opcao == 3:
        campos = input("Digite os campos de busca separados por vírgula: ").split(", ")
        valores = []
        for campo in campos:
            valor = input(f"Digite o valor para o campo '{campo}': ")
            valores.append((campo, valor))
        
        for nome, usuario in banco_usuarios.items():
            match = True
            for campo, valor in valores:
                if campo not in usuario or usuario[campo] != valor:
                    match = False
                    break
            if match:
                print(f"Nome: {nome}, Dados: {usuario}")
    elif opcao == 4:
        nomes = input("Digite os nomes separados por vírgula: ").split(", ")
        campos = input("Digite os campos de busca separados por vírgula: ").split(", ")
        valores = []
        for campo in campos:
            valor = input(f"Digite o valor para o campo '{campo}': ")
            valores.append((campo, valor))
        
        for nome in nomes:
            if nome in banco_usuarios:
                usuario = banco_usuarios[nome]
                match = True
                for campo, valor in valores:
                    if campo not in usuario or usuario[campo] != valor:
                        match = False
                        break
                if match:
                    print(f"Nome: {nome}, Dados: {usuario}")
    else:
        print("Opção inválida!")

#Programa principal
def main():
    """ 
    Esse é o loop principal da aplicação, funciona como o menu que permite chamar as funções de cadastrar usuário e imprimir usuários ou finalizr o programa com base no input. 
    """ 
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(", ")
    
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")


main()
