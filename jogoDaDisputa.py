from copy import deepcopy
from random import randint
from pilha import Pilha
from kard import Kard
from jogador import Jogador
from indefnido import *
from pickle import *



# ______________________________________________________________________________________________________________________
#                                                Lendo o arquivo de cartas

ckard = lerArquivo('Cartas.txt')

#  desagrupa os dados
ckard = separarDados(ckard)
ckard.pop(0)  # Elimina primeira linha com dados desnecessarios
embaralhar(ckard)  # embaralhar as caras

cartas = Pilha()  # Cria uma pilha
for kardd in ckard:  # Adicionano cartas na pilha
    # Lendo informações da carta
    a = kardd[0] 
    b = kardd[1]
    c = kardd[2]
    d = kardd[3]
    e = kardd[4]

    f = Kard(a, b, c, d, e)  # Criando objeto carta
    cartas.poe(f)  # Adicionado na pilha

# ______________________________________________________________________________________________________________________
#                                       Definindo modo de jogo


# inserir o modo de jodo
modoDeJogo = int(input('____| Modo de Jogo |____ \n\n\t[1] - Modo manual \n\t[0] - Modo aleatório \n\nEscolha o modo de jogo: '))   # 1 representa o modo manual e 0 o modo automatico
print('\n')
# ______________________________________________________________________________________________________________________
#                                        Cadastrando (ou logando) jogadores

Jogador1 = None
Jogador2 = None
inexixtenciadoarquivo = False  #  Identifica se há um arquivo de cadastros
players = []

try:
    arquivo = open('dementador.riddle', 'rb')
except:
    inexixtenciadoarquivo = True
    arquivo = open('dementador.riddle', 'wb')

if inexixtenciadoarquivo:
    nick = input('Jogador 1, digite seu nick: ')
    print('Jogador novo. Cadastrado!')
    print('\n')
    Jogadorr = Jogador(nick)
    players.append(Jogadorr)
    dump(players, arquivo)
    arquivo.close()
    Jogador1 = procurarJogador(players, nick)
else:
    try:
        players = load(arquivo)
        arquivo.close()
    except EOFError:
        players = []
    nick = input('Jogador 1, digite seu nick: ')
    Jogador1 = procurarJogador(players, nick)
    if Jogador1 or Jogador1 == 0:
        print('\n')
        print(players[Jogador1].get_status())
        print('\n')
    else:
        print('Jogador novo. Cadastrado!')
        print('\n')
        Jogadorr = Jogador(nick)
        players.append(Jogadorr)
        Jogador1 = procurarJogador(players, nick)

nick = input('Jogador 2, digite seu nick: ')
Jogador2 = procurarJogador(players, nick)
if Jogador2 or Jogador2 == 0:
    print('\n')
    print(players[Jogador2].get_status())
    print('\n')
else:
    print('Jogador novo. Cadastrado!')
    print('\n')
    Jogadorr = Jogador(nick)
    players.append(Jogadorr)
    Jogador2 = procurarJogador(players, nick)

# ______________________________________________________________________________________________________________________

j1Mão = [0, 0, 0, 0, 0,]
j2Mão = [0, 0, 0, 0, 0,]
qtDisputasj1 = 0
qtDisputasj2 = 0

# ______________________________________________________________________________________________________________________
#                                   Distribuindo as cartas para os jogadores
for i in range(5):
    j1Mão[i] = cartas.tira()
    j2Mão[i] = cartas.tira()
# ______________________________________________________________________________________________________________________
#                                           Escolha do tipo da disputa
for nm in range(10):
    # Seleciona o tipo de disputa
    if nm % 2 == 0:
        jogadorAtual = 'Jogador 1'
    else:
        jogadorAtual = 'Jogador 2'
    print('\n_____| Escolha da disputa: |_____\n\n')
    print('[1] - Valor')
    print('[2] - Força')
    print('[3] - Energia')
    print('[4] - Jokempô')
    tipoDeDisputa = int(input('\n{} escolha a disputa: '.format(jogadorAtual)))
    print('\n\n')
# ______________________________________________________________________________________________________________________

    if modoDeJogo == 1:
        ordenar(j1Mão, 0)  # Ordenando
        ordenar(j2Mão, 0)
    elif modoDeJogo == 0 and 0 < tipoDeDisputa < 4:
        ordenar(j1Mão, tipoDeDisputa)  # Ordenando
        ordenar(j2Mão, tipoDeDisputa)
    else:
        embaralhar(j1Mão)
        embaralhar(j2Mão)
    # __________________________________________________________________________________________________________________
    #                            Apenas exibindo as cartas dos jogadores para verificação

    print('Jogador 1: ')
    print('Disputas ganhas: {}'.format(qtDisputasj1))
    print('Cartas: \n') 
    p = 0              
    for c in j1Mão:                      
        print('[{}] - {}'.format(p, c.get_carta()))
        p += 1            
    print('\n')                         
    print('Jogador 2: ') 
    print('Disputas ganhas: {}'.format(qtDisputasj2))
    print('Cartas: \n') 
    p = 0        
    for c in j2Mão:        
        print('[{}] - {}'.format(p, c.get_carta()))
        p += 1
    print('\n')            
    # __________________________________________________________________________________________________________________
    #                                    Selecionar carta jogada de acordo com o modo de jogo

    if modoDeJogo == 0:
        cartaSorteadaP1 = randint(0, len(j1Mão) - 1)
        cartaSorteadaP2 = randint(0, len(j2Mão) - 1)
    else:
        cartaSorteadaP1 = int(input('Jogador 1 digite a posição da carta: '))
        cartaSorteadaP2 = int(input('Jogador 2 digite a posição da carta: '))

    # __________________________________________________________________________________________________________________

    h = j1Mão[cartaSorteadaP1]
    j = j2Mão[cartaSorteadaP2]
    print('\n\n')
    print('Carta selecionada do jogador 1: ', h.get_carta())
    print('Carta selecionada do jogador 2: ', j.get_carta())
    print('\n\n')
    n = comparar(h, j, tipoDeDisputa)  # Comparando

    j1Mão.pop(cartaSorteadaP1)  # descarta a carta jogada
    j2Mão.pop(cartaSorteadaP2)  # descarta a carta jogada
# ______________________________________________________________________________________________________________________
# 
    if n == h:
        print('jogador 1 ganhou a disputa!')
        j2Mão.append(cartas.tira())  # Adiciona uma nova carta para o jogador perdedor
        qtDisputasj1 += 1
    elif n == j:
        print('jogador 2 ganhou a disputa!')
        j1Mão.append(cartas.tira())  # Adiciona uma nova carta para o jogador perdedor
        qtDisputasj2 += 1
    elif n == 'empate':
        print('a disputa terminou em empate.')
        j1Mão.append(cartas.tira())  # Adiciona uma nova carta para o jogador perdedor
        j2Mão.append(cartas.tira())  # Adiciona uma nova carta para o jogador perdedor
    
    if len(j1Mão) == 0 or len(j2Mão) == 0:
        break

players[Jogador1].adicionarPartida()
players[Jogador2].adicionarPartida()
# ______________________________________________________________________________________________________________________
#                           Define o vencedor do jogo (quem tiver ficado sem cartas) 
if len(j1Mão) == 0:
    print('{} é o ganhador do jogo'.format(players[Jogador1].get_nick()))
    players[Jogador1].adiconarVitorias()
elif len(j2Mão) == 0:
    print('{} é o ganhador do jogo'.format(players[Jogador2].get_nick()))
    players[Jogador2].adiconarVitorias()
# ______________________________________________________________________________________________________________________
#                       Define (se houver) o ganhador do jogo em caso de empate

elif len(j1Mão) != 0 and len(j2Mão) != 0:  # Desempata caso os dois jogadores ainda tenham cartas
    j1Desempate = 0
    j2Desempate = 0
    for i in range(len(j1Mão)):
        j1Desempate = j1Desempate + int(j1Mão[i].get_valor())
    for m in range(len(j2Mão)):
        j2Desempate = j2Desempate + int(j2Mão[i].get_valor())

    if j1Desempate < j2Desempate:
        print('{} é o ganhador do jogo'.format(players[Jogador1].get_nick()))
        players[Jogador1].adiconarVitorias()
    elif j1Desempate > j2Desempate:
        print('{} é o ganhador do jogo'.format(players[Jogador2].get_nick()))
        players[Jogador2].adiconarVitorias()

    elif j1Desempate == j2Desempate:
        for i in range(len(j1Mão)):
            j1Desempate = j1Desempate + float(j1Mão[i].get_força())
        for m in range(len(j2Mão)):
            j2Desempate = j2Desempate + float(j2Mão[i].get_força())
    
        if j1Desempate < j2Desempate:
            print('{} é o ganhador do jogo'.format(players[Jogador1].get_nick()))
            players[Jogador1].adiconarVitorias()
        elif j1Desempate > j2Desempate:
            print('{} é o ganhador do jogo'.format(players[Jogador2].get_nick()))
            players[Jogador2].adiconarVitorias()

        elif j1Desempate == j2Desempate:
            for i in range(len(j1Mão)):
                j1Desempate = j1Desempate + float(j1Mão[i].get_energia())
            for m in range(len(j2Mão)):
                j2Desempate = j2Desempate + float(j2Mão[i].get_energia())

            if j1Desempate < j2Desempate:
                print('{} é o ganhador do jogo'.format(players[Jogador1].get_nick()))
                players[Jogador1].adiconarVitorias()
            elif j1Desempate > j2Desempate:
                print('{} é o ganhador do jogo'.format(players[Jogador2].get_nick()))
                players[Jogador2].adiconarVitorias()
            else:
                print('Não Houve ganhador')
# ______________________________________________________________________________________________________________________


arquivo = open('dementador.riddle', 'wb')
dump(players, arquivo)  # Salva os dados do jogo
