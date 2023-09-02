
num_linhas = int(input("Digite o número que será o tamanho do tabuleiro: "))
num_colunas = num_linhas

#Declarando o formato do tabuleiro
tabuleiro = {}

for linha in range(num_linhas):
    for coluna in range(num_colunas):
        tabuleiro[(linha, coluna)] = "-"

#Função para impressão do tabuleiro
def imprimir_tabuleiro():
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            print(tabuleiro[(linha, coluna)], end=" ")
        print()

#Função de verificação das condições de vitória
def verificar_vitoria(jogador):
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
    while True:
        coordenadas = input(f"Jogador {jogador}, digite as coordenadas com espaço (linha coluna): ")
        try:
            linha, coluna = map(int, coordenadas.split())
            if 0 <= linha < num_linhas and 0 <= coluna < num_colunas and tabuleiro[(linha, coluna)] == "-":
                tabuleiro[(linha, coluna)] = "X" if jogador == 1 else "O"
                break
            else:
                print("Posição já ocupada. Tente novamente!!")
        except ValueError:
            print("Coordenadas inválidas, o formato é 'linha coluna'.")

#Inicia o jogo
print(f"Boas vindas ao jogo da velha {num_linhas}x{num_colunas}! O Jogador 1 é representado pelo X e o Jogador 2 pelo O!")
vitoria = False
jogador_atual = 1

while not vitoria:
    imprimir_tabuleiro()
    #Verif condição de vitória
    if verificar_vitoria("X"):
        print("O Jogador 1 (X) ganhou!")
        vitoria = True
    elif verificar_vitoria("O"):
        print("O Jogador 2 (O) ganhou!")
        vitoria = True
    elif all(tabuleiro[coord] != "-" for coord in tabuleiro):
        print("Deu velha! O jogo empatou.")
        vitoria = True
    else:
        fazer_jogada(jogador_atual)
        jogador_atual = 3 - jogador_atual  #alternar jogadores
