#Exercício 3 - Jogo Termo
"""
Neste exercício, foram importadas as bibliotecas e tecnologias necessárias, sendo elas para gerar um número aleatório, ler arquivos de texto e depois colorir os textos no console.
O funcionamento do jogo Termo é bem semelhante ao jogo da Forca, então o código foi reutilizado e reestruturado para adaptar ao jogo novo, porém, sendo sempre para palavras de 5 letras.
O código escolhe uma palavra aleatória de 5 letras e gera um output com 5 espaços vazios representados por _ . Quando o jogo inicia o usuário tem 6 vidas e precisa dar um palpite de uma palavra de 5 letras.
O palpite do usuário e suas respectivas letras são armazenados para serem impressos de volta depois de passarem por uma condicional que funciona da seguinte maneira: 
Se as letras da palavra escolhida tiverem na palavra secreta na posição correta, serão impressas de volta porém pintadas de verde e caso estejam na palavra porém na posição errrada, são impressas de amarelo.
Conforme as tentativas vão ocorrendo, é descontada uma vida e as palavras digitadas anteriormente são impressas de volta.
O jogo acaba quando as vidas se esgotarem ou quando a palavra digitada for igual a palavra secreta.
"""


#Fazendo importações das tecnologias necessárias
#termcolor instalado via pip install termcolor
import os
import random
from termcolor import colored


def le_arquivo(arq):
    """
    Função para ler o arquivo e retornar uma lista formatada com todas as linhas
    """
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]


def gera_lista_n_letras(lista, n):
    """
    Gera uma lista de palavras com um comprimento específico (adaptado do código do jogo da forca)
    """
    return [x for x in lista if len(x) == n]


def imprime_palavra_atual(palavra_atual, palavra):
    """
    Percorre a palavra para imprimir com cores com as condições de: verde = letra correta na posição correta; amarelo = letra correta na posição errada. 
    """
    output = ""
    for i in range(len(palavra)):
        if palavra_atual[i] == palavra[i]:
            output += colored(palavra_atual[i], 'green') + " "
        elif palavra_atual[i] in palavra:
            output += colored(palavra_atual[i], 'yellow') + " "
        else:
            output += colored(palavra_atual[i], 'red') + " "
    print(output)

#Configurações iniciais
arquivo = "lista_palavras.txt"
lista = le_arquivo(arquivo)
tamanho_palavra = 5
lista_n = gera_lista_n_letras(lista, tamanho_palavra)
palavra = list(random.choice(lista_n))
palavra_atual = ["_"] * tamanho_palavra

#Iniciando o jogo
print("Bem vindo ao jogo Termo!")
#Definindo a quantidade de vidas e a lista para exibir palavras que ja foram palpitadas anteriormente
vidas = 6
tentativas = []

#Definindo a condição para rodar o loop do jogo
while vidas > 0:
    imprime_palavra_atual(palavra_atual, palavra)
    
    #percorrendo tentativas anteriores para exibir na tela
    if tentativas:
        print("Tentativas anteriores:")
        for t in tentativas:
            t_str = ""
            for letra in t:
                t_str += letra + " "
            print(t_str)
    
    palpite = input("Digite um palpite de 5 letras: ")

    #mensagem de erro caso o usuário digite um palpite com quantidade de letras erradas
    if len(palpite) != tamanho_palavra:
        print("Por favor, digite um palpite com 5 letras.")
        continue

    sucesso = False
    for i in range(tamanho_palavra):
        if palpite[i] == palavra[i]:
            sucesso = True
            palavra_atual[i] = palpite[i]
        elif palpite[i] in palavra:
            print(colored(palpite[i], 'yellow'), end=" ")
        else:
            print(colored(palpite[i], 'red'), end=" ")
    
    tentativas.append(list(palpite))

    #condição de vitória, comparando letra por letra da palavra atual e a palavra escolhida
    if all(palavra_atual[i] == palavra[i] for i in range(len(palavra))):
        print(f"Você ganhou! A palavra era:{palavra}")
        break

    #descontando uma vida a cada rodada e imprimindo
    vidas -= 1
    print("")
    print(f"Vidas restantes: {vidas}")

#fim de jogo caso o usuário perca
if vidas == 0:
    print(f"Você perdeu. A palavra era:{palavra}")