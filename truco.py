'''
Projeto: Truco - V.1.0
2025.06.25
Luiz Otávio de Souza Freo
'''

# Objetivo: Desenvolver um projeto que simule uma partida de truco 1x1, onde o jogador receberá 3 cartas e jogará contra o computador (Bot) que também receberá 3 cartas. A partida acaba quando um dos dois atirgir a pontuação 12.

# BIBLIOTECAS --> Espaço reservado para a declaração das bibliotecas e funções
from random import randint         # importa a função randint que sorteia um número aleatório
from time import sleep             # importa a função sleep que faz pausas no jogo

# CONSTANTES --> Espaço reservado para a declaração de constantes
TAM = int(50)           # tamanho da linha
TEM = int(2)            # tempo de espera curto
ESP = int(5)            # tempo de espera longo
CAR = '-'               # caractere da linha
MAX = int(6)            # máximo de trentos do jogo

# VARIÁVEIS --> Espaço reservado para a declaração de variáveis
esc = 0                 # variável da escolha que o Jogador faz
num = 0                 # variável para armazenar o número de uma carta aleatória do baralho que será usada para definir a manilha
posicao = 0             # variável da posição de 'num' na ordem das cartas do baralho, que também será usada para definir a manilha
pontosJg = 0            # variável de contagem dos pontos da rodada do Jogador
pontosBot = 0           # variável de contagem dos pontos da rodada do Bot
tentosJg = 0           # variável de contagem dos trentos do Jogador
tentosBot = 0          # variável de contagem de trentos do Bot
pCartaJg = 0            # variável da posição da carta ecolhida pelo Jogador na lista de cartas dele
pCartaBot = 0           # variável da posição da carta escolhida pelo Bot na lista de cartas dele
partida = 0             # variável da contagem das partidas
torne = 0               # variável que define quem tornará na partida, sendo 0 == Jogador, e 1 == Bot
pRod = 1                # variável que define quem fez a primeira rodada em casa de empates, sendo 0 == Jogador, 1 == Bot, e 2 == Empate
cartaJg = ''            # variável da carta que o Jogador escolheu jogar
cartaBot = ''           # variável da carta que o Bot escolheu jogar
manilha = ''            # variável da manilha do jogo              
msg = ''                # variável que armazena a msg a ser mostrada na tela
resultado = ''          # variável que armazena o resultado da rodada
vencedor = ''           # variável que armazena o vencedor do Jogo

# LISTAS --> Espaço resenvado para a declaração de listas
MSGS = []               # lista de msgs


CARTAS = ['A ♦', 'A ♠', 'A ♥', 'A ♣',                             # lista de cartas base do baralho
          '2 ♦', '2 ♠', '2 ♥', '2 ♣', 
          '3 ♦', '3 ♠', '3 ♥', '3 ♣', 
          '4 ♦', '4 ♠', '4 ♥', '4 ♣', 
          '5 ♦', '5 ♠', '5 ♥', '5 ♣', 
          '6 ♦', '6 ♠', '6 ♥', '6 ♣', 
          '7 ♦', '7 ♠', '7 ♥', '7 ♣', 
          'Q ♦', 'Q ♠', 'Q ♥', 'Q ♣', 
          'J ♦', 'J ♠', 'J ♥', 'J ♣', 
          'K ♦', 'K ♠', 'K ♥', 'K ♣',]

cartas = ['A ♦', 'A ♠', 'A ♥', 'A ♣',                             # lista de cartas do baralho para ser manipulada
          '2 ♦', '2 ♠', '2 ♥', '2 ♣', 
          '3 ♦', '3 ♠', '3 ♥', '3 ♣', 
          '4 ♦', '4 ♠', '4 ♥', '4 ♣', 
          '5 ♦', '5 ♠', '5 ♥', '5 ♣', 
          '6 ♦', '6 ♠', '6 ♥', '6 ♣', 
          '7 ♦', '7 ♠', '7 ♥', '7 ♣', 
          'Q ♦', 'Q ♠', 'Q ♥', 'Q ♣', 
          'J ♦', 'J ♠', 'J ♥', 'J ♣', 
          'K ♦', 'K ♠', 'K ♥', 'K ♣',]

ordem = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']        # lista com a ordem padrão das cartas do baralho
FORTES = ['3', '2', 'A', 'K', 'J', 'Q', '7', '6', '5', '4']       # lista com a ordem de força base (sem considerar a manilha) das cartas
fortes = ['3', '2', 'A', 'K', 'J', 'Q', '7', '6', '5', '4']       # lista com a ordem de força das cartas
naipes = ['♣', '♥', '♠', '♦']                                     # lista com os naipes das cartas
msgsCab = ['TRUCO', 'Desenvolvido por Luiz Otávio']               # lista com as msgs do cabeçalho
msgsMenu = ['Seja Bem Vindo!', 'A partida começará em breve...']  # lista com as msgs do menu inicial

cartasJg = []           # lista das cartas do Jogador
cartasBot = []          # lista das cartas do Bot
opcoes = []             # lista das opções do Jogador

# FUNÇÕES DO PROJETO --> Espaço reservado para a declaração das funções do projeto
# Função para limpar a tela
def limpaTela():
    print('\n'*TAM)            # quebra a linha TAM (50) vezes 

# Função para desenhar uma linha
def mostraLinha():
    print(f'{CAR}'*TAM)        # mostra CAR (-) TAM (50) vezes na linha, fazendo uma linha de caracteres

# Função para mostrar uma MSG Centralizada
def msgCentro(msg):
    print(f'{msg:^{TAM}}')     # mostra uma msg centralizada no meio de uma linha com TAM (50) caracteres

# Função para mostrar uma MSG a Esquerda
def msgEsquerda(msg):
    print(f'{msg:<{TAM}}')     # mostra uma msg a esquerda da tela

# Função para mostrar Cabeçalho
def mostraCabecalho(MSGS):
    mostraLinha()              # mostra uma linha de caracteres
    for msg in MSGS:           # repete para cada msg que tiver sido passada como parâmetro
        msgCentro(msg)         # mostra uma msg centralizada
    mostraLinha()              # mostra uma linha de caracteres

# Função para mostrar Msgs
def mostraMsgs(MSGS):
    mostraLinha()              # mostra uma linha de caracteres
    for msg in MSGS:           # repete para cada msg que tiver sido passada como parâmetro
        msgEsquerda(msg)       # mostra uma msg a esquerda
    mostraLinha()              # mostra uma linha de caracteres

# Função para distribuir as cartas
def disCartas():
    for i in range(3):                      # repete 3 vezes, distribuindo 1 carta para o Jogador e 1 carta para o Bot de cada vez
        carta = randint(0, 39-i-i)          # seleciona uma carta aleatória do baralho
        cartasJg.append(cartas[carta])      # adiciona a carta selecionada às cartas do Jogador
        cartas.pop(carta)                   # retira a carta selecionada do baralho

        carta = randint(0, 39-i-i-1)        # seleciona uma carta aleatória do baralho
        cartasBot.append(cartas[carta])     # adiciona a carta selecionada às cartas do Bot
        cartas.pop(carta)                   # retira a carta selecionada do baralho

# Função para receber a escolha do Jogador
def getValue(msg):
    esc = input(f'{msg}: ').strip()         # mostra uma msg e lê a escolha do Jogador desconsiderando os espaços
    return esc                              # reorna a escolha do Jogador

# Função para validar os Valores
def validaValue(esc, opcoes):
    if esc in opcoes:        # verifica se a escolha do Jogador está entre as opções
        return True           # caso esteja retorna True (Verdade)
    
    else:                     # caso contrário

        MSGS = [f'{esc} não é uma opção válida!',     # define as MSGS, dizando que o valor digitado não é válido
                f'Escolha entre {opcoes}']
        
        mostraMsgs(MSGS)      # mostra as msgs
        return False          # retorna False (Falso)

# Fução para selecionar a Manilha
def selManilha():
    num = cartas[randint(0, 33)]        # escolhe uma carta aleatória entre as que sobraram para 'virar'
    num = num[0]                        # pega só o valor da carta (2, 7, K etc)
    posicao = ordem.index(num)          # encontra a posição dessa carta na ordem do baralho
    posicao += 1                        # escolhe a carta seguinte da ordem para ser a manilha
    if posicao > len(ordem)-1:          # verifica se a posição seguinte está fora da lista (no caso do K que é a última carta, a manilha deve ser o A que é a primeira)
        posicao = 0                     # caso esteja fora da lista, a posição vira a primeira (ou seja, a manilha será A)
    manilha = ordem[posicao]            # manilha recebe a carta da 'posicao' em 'ordem'
    
    posicao = FORTES.index(manilha)     # encontra a manilha na ordem das cartas fortes do baralho
    fortes.pop(posicao)                 # retira a manilha da posição original
    fortes.insert(0, manilha)           # insere a manilha na posição 0, ou seja, torna a manilha a carta mais forte do baralho

# Função da jogada do Jogador
def jogadaJg(MSGS, opcoes):
    mostraCabecalho(MSGS)                         # mostra as MSGS pré-definidas no cabeçalho
    msg = '--> Sua escolha'                       # define a msg que será mostrada
    esc = getValue(msg)                           # armazena a escolha do Jogador

    while not validaValue(esc, opcoes):           # valida a escolha do Jogador
        esc = getValue(msg)

    pCartaJg = int(esc)-1                         # define a posição da carta que o Jogador escolheu
    cartaJg = cartasJg[pCartaJg]                  # define a carta que o Jogador escolheu
    cartasJg.pop(pCartaJg)                        # remove a carta escolhida das cartas do Jogador
    mostraCabecalho([f'Jogador jogou {cartaJg}']) # mostra msg dizando qual carta o Jogador jogou
    sleep(TEM)                                    # espera um tempo
    return cartaJg                                # retorna a carta escolhida pelo jogador

# Função da jogada do Bot
def jogadaBot():
    mostraCabecalho(['Bot está pensando...'])     # mostra msg
    sleep(TEM)                                    # espera um tempo
    pCartaBot = randint(0, len(cartasBot)-1)      # define a posição de uma carta aleatória entre as que o Bot possuí
    cartaBot = cartasBot[pCartaBot]               # define a carta que o Bot escolheu
    cartasBot.pop(pCartaBot)                      # remove a carta escolhida das cartas do Bot
    mostraCabecalho([f'Bot jogou {cartaBot}'])    # mostra msg dizendo qual carta o Bot jogou
    sleep(TEM)                                    # espera um tempo
    return cartaBot                               # retorna a carta escolhida pelo Bot

# Função para rezetar o Baralho
def juntarBaralho():
    for i in range(len(cartas)):        # repete para todas as cartas do baralho
        cartas.pop(0)                   # retira elas do baralho
    for i in range(len(CARTAS)):        # repete para todas as cartas do baralho Base
        cartas.append(CARTAS[i])        # duplica as cartas do baralho Base para o baralho do Jogo
        
# Função para verificar quem ganhou
def ganhou(cartaJg, cartaBot):
    if fortes.index(cartaJg[0]) < fortes.index(cartaBot[0]):         # verifica se a carta escolhida pelo jogador é mais forte que a carta escolhida pelo Bot
        resultado = 'Ganhador: Jogador'            # caso retorne True (Verdade), o Jogador é o ganhador da rodada

    elif fortes.index(cartaBot[0]) < fortes.index(cartaJg[0]):       # caso retorne False (Falso), verifica se a carta do Bot é mais forte que a carta do Jogador
        resultado = 'Ganhador: Bot'   # caso retorne True (Verdade), o Bot é o ganhador da rodada

    else:                  # caso retorne Fase (Falso), significa que o valor das cartas é igual
        if cartaJg[0] == manilha:       # verifica se a carta é uma manilha

            if naipes.index(cartaJg[2]) < naipes.index(cartaBot[2]): # Caso retorne True (Verdade), verifica se o naipe do Jogador é melhor que o naipe do Bot
                resultado = 'Ganhador: Jogador'    # caso retorne True (Verdade), o Jogador é o ganhador da rodada

            else:                       # caso retorne False (Falso)
                resultado = 'Ganhador: Bot'        # o Bot é o ganhador da rodada
        
        else:              # caso retorne False (Falso), ou seja, caso haja um empate
            resultado = 'Empate'        # o resultado é um Empate
    
    return resultado                    # retorna o resultado do ganhador

# Função principal do jogo
def jogar():

    # Menu Inicial do Jogo
    global manilha, cartas, fortes, tentosJg, tentosBot, ganhador, cartasJg, cartasBot    # tranforma essas variáveis em variáveis globais

    limpaTela()                # limpa a tela
    mostraCabecalho(msgsCab)   # mostra o cabeçalho do Jogo
    mostraMsgs(msgsMenu)       # mostra as msgs do Menu inicial
    sleep(ESP)                 # espera um tempo

    MSGS = ['Tudo pronto.',    # define as MSGS
            'Iniciando partida contra Bot...']
    
    mostraMsgs(MSGS)           # mostra as MSGS
    sleep(ESP)                 # espera um tempo

    # Partidas
    partida = 1             # define a partida como 1

    while (tentosJg < MAX) and (tentosBot < MAX): # repete até que o Jogador ou o Bot atinjam 12 trentos
        
        cartasJg = []           # zera as cartas do Jogador
        cartasBot = []          # zera as cartas do Bot

        fortes = ['3', '2', 'A', 'K', 'J', 'Q', '7', '6', '5', '4'] # rezeta a lista de cartas fortes, ou seja, a deixa sem a manilha

        juntarBaralho()     # rezeta o baralho
        disCartas()         # distribui as cartas
        selManilha()        # seleciona a manilha
        limpaTela()         # limpa a tela

        # Rodadas
        pontosJg = 0        # zera os pontos do Jogador que serão usados na rodada
        pontosBot = 0       # zera os pontos do Bot que serão usados na rodada
        torne = 0           # define a variável torne como 0, ou seja, o Jogador começará jogando na rodada

        for i in range(3):  # repete no máximo 3 vezes, cada vez corresponde a uma rodada

            # Cabeçalho inicial
            mostraCabecalho(msgsCab)                                        # mostra o Cabeçalho
            mostraCabecalho([f'Partida n° {partida}', f'{i+1}° rodada'])    # mostra a partida e a rodada atuais
            sleep(TEM)                                                      # espera um tempo
            mostraCabecalho([f'A manilha é: {fortes[0]}'])                  # mostra a manilha da partida

            # Definição das MSGS da rodada
            if i == 0:      # verifica se a rodada é a primeira

                opcoes = ['1', '2', '3']    # caso retorne True (Verdade); significa que o jogador ainda tem 3 cartas
                MSGS = ['Escolha uma opção:', f'[1] {cartasJg[0]}  [2] {cartasJg[1]}  [3] {cartasJg[2]}'] # define as msgs com as opções do Jogador

            elif i == 1:    # Caso retorne False (Falso); verifica se é a segunda rodada

                opcoes = ['1', '2']         # caso retorne True (Verdade); significa que o Jogador jogou 1 carta, ou seja, ele tem 2 cartas
                MSGS = ['Escolha uma opção:', f'[1] {cartasJg[0]}  [2] {cartasJg[1]}']  # define as msgs com as opções do Jogador

            else:           # Caso retorne False (Falso); significa que é a última rodada
                opcoes = ['1']              # como é a última rodada o Jogador tem apenas 1 carta, ou seja, 1 escolha apenas
                MSGS = ['Escolha uma opção:', f'[1] {cartasJg[0]}'] # define as msgs com as opções do Jogador

            # Verificação de quem deve tornar
            if torne == 0:
                cartaJg = jogadaJg(MSGS, opcoes)        # jogada do Jogador
                cartaBot = jogadaBot()                  # jogada do Bot
            else:
                cartaBot = jogadaBot()                  # jogada do Bot
                cartaJg = jogadaJg(MSGS, opcoes)        # jogada do Jogador

            # Resultado da rodada
            resultado = ganhou(cartaJg, cartaBot)       # calcula o ganhador da rodada
            mostraCabecalho([f'{resultado}'])           # mostra o ganhador da rodada
            sleep(ESP)                                  # espera um tempo

            if resultado == 'Ganhador: Jogador':        # verifica se o ganhador da rodada foi o Jogador
                pontosJg += 1           # caso retorne True (verdade) o Jogador ganha 1 ponto
                torne = 0               # como o Jogador ganhou ele deverá iniciar a próxima rodada, por isso torne recebe 0
                if i == 0:              # verifica se a rodada que o Jogador ganhou foi a primeira (isso servirá como critério de desempate)
                    pRod = 0            # caso retorne True (Verdade); o Jogador ganhou a primeira rodada, por isso pRod recebe 0
                if pRod == 2:           # verifica se a primeira partida empatou
                    break               # caso retorne True (Verdade); encerra a partida

            elif resultado == 'Ganhador: Bot':          # caso retorne False (Falso); verifica se o ganhador da rodada foi o Bot
                pontosBot += 1          # caso retorne True (Verdade); o Bot ganha 1 ponto
                torne = 1               # como o Bot ganhou ele deverá iniciar a próxima rodada, por isso torne recebe 1
                if i == 0:              # verifica se a rodada que o Bot ganhou foi a primeira (isso servirá como critério de desempate)
                    pRod = 1            # caso retorne True (Verdade); o Jogador ganhou a primeira rodada, por isso pRod recebe 0
                if pRod == 2:           # verifica se a primeira partida empatou
                    break               # caso retorne True (Verdade); encerra a partida

            else:               # caso retorne False (Falso); significa que a rodada empatou
                if i == 0:      # nesse caso, verifica se a rodada de empate foi a primeira
                    pRod = 2    # caso retorne True (Verdade); pRod recebe 2, ou seja, empate (isso serve para que na próxima rodada, caso não haja empate a partida seja encerrada)

            if (pontosJg == 2) or (pontosBot == 2):     # verifica se algum dos jogadores atingiu 2 pontos
                break           # caso retorne True (Verdade); encerra a partida
        
        # Verificação de quem venceu a partida e ganhou os tentos
        if pontosJg > pontosBot:        # verifica se a qtd de pontos do Jogador é maior que a qtd de pontos do Bot
            tentosJg += 1               # caso retorne True (Verdade); o Jogador ganha os tentos da partida

        elif pontosBot > pontosJg:      # caso retorne False (Falso); verifica se a qtd de pontos do Bot é a maior que a qtd de pontos do Jogador
            tentosBot += 1              # caso retorne True (Verdade); o Bot ganha os tentos da partida

        else:               # caso retorne False (Falso); significa que houve um empate, nesse caso ganha os pontos quem ganhou a primeira rodada

            if pRod == 0:               # verifica se o Jogador ganhou a primeira rodada
                tentosJg += 1           # caso retorne True (Verdade); o Jogador ganha os tentos da partida

            else:                       # caso retorne False (Falso)
                tentosBot += 1          # o Bot ganha os tentos da partida
        
        # Placar do final da partida
        partida += 1                # soma 1 à variável partida
        limpaTela()                 # limpa a Tela
        mostraCabecalho(msgsCab)    # mostra o Cabeçalho

        mostraCabecalho([f'Tentos Jogador: {tentosJg}', f'Tentos Bot: {tentosBot}'])    # mostra o placar

        sleep(ESP)                  # espera um tempo

    # Verificação quem venceu o Jogo
    if tentosJg > tentosBot:    # verifica se a qtd de tentos do Jogador é maior que a qtd de tentos do Bot
        vencedor = 'Jogador'    # caso retorne True (Verdade); o vencedor do Jogo é o Jogador

    else:                       # caso retorne False (Falso)
        vencedor = 'Bot'        # o vencedor do Jogo é o Bot

    # MSGS finais
    limpaTela()                 # limpa a Tela
    mostraCabecalho(msgsCab)    # mostra o Cabeçalho

    MSGS = ['Fim de Jogo!!!', '', 'Placar final:', f'Tentos Jogador: {tentosJg}', f'Tentos Bot: {tentosBot}', f'Vencedor: {vencedor}'] # define as MSGS finais

    mostraCabecalho(MSGS)       # mostra as MSGS finais
    sleep(ESP)                  # espera um tempo

    mostraCabecalho(['Obrigado por jogar!!!'])  # mostra msg de agradecimento


# Início do Jogo
jogar()  # chama a função jogar
