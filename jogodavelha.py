import random

#tabuleiro
tabuleiro = [['', '', ''],
          ['', '', ''],
          ['', '', '']]

#variaveis para guardar as pontuações
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
    print(f'{tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}')
    print(f'{tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}')
    print(f'{tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}')
    
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
    return 0 <= linha < 3 and 0 <= coluna <3 and tabuleiro[linha][coluna] == ''


#realizar jogada
def jogar(jogador, linha, coluna):
    tabuleiro[linha][coluna] = jogador

#jogada do usuário
def jogada_usuario(jogador):
    linha = coordenada_linha()
    coluna = coordenada_coluna()
    if posicao_valida(linha, coluna):
        jogar(jogador, linha, coluna)
    else: print('Jogada inválida! Por favor, escolha outra.')

#verificar se há uma sequência de 3 x ou o em qualquer direção
def verificar_vencedor():
    for i in range(3):
        if tabuleiro [i][0] == tabuleiro[i][1] == tabuleiro[i][2] != '':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro [2][i] != '':
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
        linha = coordenada_linha()
        coluna = coordenada_coluna()
        
        if posicao_valida(linha, coluna):
            jogar(jogador_atual, linha, coluna) #função de fazer a jogada
            
            vencedor = verificar_vencedor()
            if vencedor:
                imprimir_tabuleiro()
                print(f'{vencedor} venceu!')
                return vencedor
            elif verificar_velha():
                imprimir_tabuleiro()
                print('Velha!')
                return None
            jogador_atual = 'O' if jogador_atual == 'X' else 'X' #if ternario para alternar entre os jogadores
        else:
            print('Posição inválida! Por favor, escolha outra.')

#jogada da máquina, fácil
def jogada_maquina_facil():
    while True:
        linha = random.randint(0,2)
        coluna = random.randint(0,2)
        if posicao_valida(linha, coluna):
            jogar('O', linha, coluna)
            break

#modo contra a máquina, fácil
def maquina_facil():
    jogador_atual = 'X' #o usuário sempre será o 'x', a máquina será o 'o'
    while True:
        imprimir_tabuleiro()

        if jogador_atual == 'X':
            linha = coordenada_linha()
            coluna = coordenada_coluna()

            if posicao_valida(linha, coluna):
                jogar(jogador_atual, linha, coluna)
            else:
                print('Posição inválida! Por favor, escolha outra.')

            vencedor = verificar_vencedor()
            if vencedor:
                imprimir_tabuleiro()
                print(f'{vencedor} venceu!')
                return vencedor
            elif verificar_velha():
                imprimir_tabuleiro()
                print('Velha!')
                return None
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'


#lógica principal do jogo
def main():
    global pontuacao_jogador_x, pontuacao_jogador_o
    
    while pontuacao_jogador_x < 3 and pontuacao_jogador_o <3:
        opcao = menu()
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
        print('Jogador X venceu o jogo!')
    else:
        print('Jogador O venceu o jogo!')

#rodar o jogo
main()
