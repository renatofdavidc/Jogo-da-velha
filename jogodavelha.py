'''
FIAP
1TDSA - Segundo semestre de 2024

Checkpoint 4
Arquivo: jogodavelha.py

Renato de Freitas David Campiteli RM 555627
Pedro Lucas de Oliveira Bezerra RM 558439
Gabriel Santos Jablonski RM 555452

04/09/2024
'''

#import do random, que é utilizado para escolher as posições aleatórias da máquina fácil
import random

#tabuleiro
tabuleiro = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

#variáveis para guardar as pontuações
pontuacao_jogador_x = 0
pontuacao_jogador_o = 0

#menu principal
def menu():
    print('======== JOGO DA VELHA ========')
    print('[1] - Multiplayer Local')
    print('[2] - VS Máquina (Fácil)')
    print('===============================')
    opcao = input('Escolha uma opção: ')
    return opcao

#inicializar o tabuleiro
def inicializar_tabuleiro():
    global tabuleiro
    tabuleiro = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]

#imprimir tabuleiro
def imprimir_tabuleiro():
    for linha in tabuleiro:
        print(' | '.join([x if x else ' ' for x in linha]))
        print('-' * 10)

#receber coordenada da linha
def coordenada_linha():
    return int(input('Escolha a linha para jogar (0, 1, 2): '))

#receber coordenada da coluna
def coordenada_coluna():
    return int(input('Agora, escolha a coluna (0, 1, 2): '))

#imprimir a pontuação de ambos jogadores
def mostrar_pontuacao():
    print('=================')
    print('====PONTUAÇÃO====')
    print('=================')
    print(f'Jogador X: {pontuacao_jogador_x} pontos')
    print(f'Jogador O: {pontuacao_jogador_o} pontos')

#verificar se a coordenada escolhida é permitida
def posicao_valida(linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ''

#realizar jogada
def jogar(jogador, linha, coluna):
    tabuleiro[linha][coluna] = jogador

#jogada do usuário
def jogada_usuario(jogador):
    while True:
        linha = coordenada_linha()
        coluna = coordenada_coluna()
        if posicao_valida(linha, coluna):
            jogar(jogador, linha, coluna)
            break
        else:
            print('Jogada inválida! Por favor, escolha outra.')

#verificar se há uma sequência de 3 x ou o em qualquer direção
def verificar_vencedor():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != '':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != '':
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        return tabuleiro[0][2]
    return None

#verificar se deu velha
def verificar_velha():
    for linha in tabuleiro:
        if '' in linha:
            return False
    return True

#modo do multijogador local (usuário x usuário)
def multiplayer():
    jogador_atual = 'X'
    while True:
        imprimir_tabuleiro()
        jogada_usuario(jogador_atual)
        
        vencedor = verificar_vencedor()
        if vencedor:
            imprimir_tabuleiro()
            print(f'{vencedor} venceu a rodada!')
            return vencedor
        elif verificar_velha():
            imprimir_tabuleiro()
            print('Velha!')
            return None
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'  # alternar entre os jogadores

#jogada da máquina, fácil
def jogada_maquina_facil():
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicao_valida(linha, coluna):
            jogar('O', linha, coluna)
            break

#modo contra a máquina, fácil
def maquina_facil():
    jogador_atual = 'X'  # o usuário sempre será o 'x', a máquina será o 'o'
    while True:
        imprimir_tabuleiro()

        if jogador_atual == 'X':
            jogada_usuario(jogador_atual)
        else:
            jogada_maquina_facil()

        vencedor = verificar_vencedor()
        if vencedor:
            imprimir_tabuleiro()
            print(f'{vencedor} venceu a rodada!')
            return vencedor
        elif verificar_velha():
            imprimir_tabuleiro()
            print('Velha!')
            return None
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

#lógica principal do jogo
def main():
    global pontuacao_jogador_x, pontuacao_jogador_o

    while True:
        opcao = menu()
        pontuacao_jogador_x = 0
        pontuacao_jogador_o = 0
        
        while pontuacao_jogador_x < 3 and pontuacao_jogador_o < 3:
            vencedor = None

            if opcao == '1':
                vencedor = multiplayer()
            elif opcao == '2':
                vencedor = maquina_facil()
            else:
                print('Opção inválida!')
                continue

            if vencedor == 'X':
                pontuacao_jogador_x += 1
            elif vencedor == 'O':
                pontuacao_jogador_o += 1

            mostrar_pontuacao()
            inicializar_tabuleiro()

        if pontuacao_jogador_x == 3:
            print(f'Jogador X venceu o jogo! ({pontuacao_jogador_x} - {pontuacao_jogador_o})')
        else:
            print(f'Jogador O venceu o jogo! ({pontuacao_jogador_o} - {pontuacao_jogador_x})')

#rodar o jogo
main()


