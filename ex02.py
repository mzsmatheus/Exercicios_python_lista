#Exercício 2 - Jogo da velha NxN
"""
Neste exercício, foi declarado um tabuleiro em formato de dicionário, como o tamanho dele é personalizado, a variável de num_linhas recebe o input do usuário e num_colunas faz referência ao número de linhas.
Foi criada uma tupla com as coordenadas para facilitar o acesso dos índices de linha e coluna, também foi declarado o valor com _ para os espaços vazios.
Logo após isso, o tabuleiro é organizado e impresso conforme as dimensões declaradas.
Quando o jogo inicia, o jogador atual é declarado como 1 para iniciar com a marcação X e a variável que determina a condição de vitória é declarada como False para o início do loop do jogo.
Para a função de jogada, são lidas as coordenadas passadas pelo usuário separadas com espaço, logo após isso elas são transformadas em int e divididas novamente para poder percorrer o tabuleiro.
É feita uma condicional para verificar se o espaço está vazio (com _ ), se estiver, é validada a condição para ver se está na vez do jogador 1 ou 2 (X ou O).
Caso a primeira condicional não seja verdadeiram, é pedido para o usuário jogar novamente. Caso o usuário passe uma coordenada que não existe, é disparada uma exceção.
Quando um jogador finaliza sua jogada, há uma função para trocar o jogador atual.
Para a finalização do jogo, a condição de vitória é dada via função, verificando se a letra do jogador (X ou O) completa uma linha, coluna ou diagonal.
No caso de nenhuma das condições de vitórias satisfeitas, se o tabuleiro inteiro for diferente de _ o jogo também é finalizado por empate.
"""
#Declarando o tabuleiro e definindo o tamanho
num_linhas = int(input("Digite o número que será o tamanho do tabuleiro: "))
num_colunas = num_linhas
tabuleiro = {}

#Criação do tabuleiro vazio do tamanho definido
for linha in range(num_linhas):
    for coluna in range(num_colunas):
        tabuleiro[(linha, coluna)] = "-"

#Função para impressão do tabuleiro
def imprimir_tabuleiro():
    """
    Nessa função, é percorrido todo o tabuleiro criado anteriormente para a impressão com todas as linhas e colunas, colocando um espaçamento no final.
    """

    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            print(tabuleiro[(linha, coluna)], end=" ")
        print()

#Função de verificação das condições de vitória
def verificar_vitoria(jogador):
    """
    Verifica se um jogador ganhou o jogo. 
    Esta função verifica as condições de vitória para o jogador, considerando as linhas, colunas e diagonais do tabuleiro. 
    É passada como argumento a letra do jogador da vez (X ou O), percorrendo todo o tabuleiro e validando todas as linhas e colunas.
    Se o jogador ganhou o jogo é retornado True, caso as condições não sejam satisfeitas, é retornado False.

    """
    #linhas e colunas
    for linha in range(num_linhas):
        if all(tabuleiro[(linha, coluna)] == jogador for coluna in range(num_colunas)) or all(tabuleiro[(coluna, linha)] == jogador for coluna in range(num_colunas)):
            return True

    #diagonais
    if all(tabuleiro[(linha, linha)] == jogador for linha in range(num_linhas)) or all(tabuleiro[(linha, num_colunas - 1 - linha)] == jogador for linha in range(num_linhas)):
        return True

    return False

#Função para fazer uma jogada
def fazer_jogada(jogador):
    """
    Função para executar a jogada do jogador atual. A variável coordenadas recebe os inputs separados com espaço e transforma em ints da respectiva linha e coluna. 
    Após isso, é validado qual será a letra que será impressa na coordenada em questão. 
    Por fim, é verificada se a posição já foi ocupada anteriormente ou se a coordenada passada é válida.
    """
    while True:
        coordenadas = input(f"Jogador {jogador}, digite as coordenadas com espaço (linha coluna): ")
        try:
            linha, coluna = map(int, coordenadas.split())
            if tabuleiro[(linha, coluna)] == "-":
                if jogador == 1:
                    tabuleiro[(linha, coluna)] = "X"
                else:
                    tabuleiro[(linha, coluna)] = "O"
                break
            else:
                print("Posição já ocupada. Tente novamente!")
        except ValueError:
            print("Coordenadas inválidas, o formato é 'linha coluna'.")

#Inicia o jogo
print(f"Boas vindas ao jogo da velha {num_linhas}x{num_colunas}! O Jogador 1 é representado pelo X e o Jogador 2 pelo O!")
vitoria = False
jogador_atual = 1

#Criando o loop do jogo
while not vitoria:
    imprimir_tabuleiro()
    #Verif condição de vitória
    if verificar_vitoria("X"):
        print("O Jogador 1 (X) ganhou!")
        vitoria = True
    elif verificar_vitoria("O"):
        print("O Jogador 2 (O) ganhou!")
        vitoria = True
    #Se todas as posições forem diferentes de _ antes do jogo acabar, é dado o empate. 
    elif all(tabuleiro[coord] != "-" for coord in tabuleiro):
        print("Deu velha! O jogo empatou.")
        vitoria = True
    else:
        fazer_jogada(jogador_atual)
        jogador_atual = 3 - jogador_atual  #alternar jogadores
