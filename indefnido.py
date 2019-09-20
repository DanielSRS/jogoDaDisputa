from copy import deepcopy
from random import randint
from kard import Kard

# ______________________________________________________________________________________________________________________

def trocarDePosicao(lista: list, AL: int, AL2: int):  # Troca de posição dois elementos de uma lista
        AX1 = lista[AL]
        AX2 = lista[AL2]
        lista[AL] = AX2
        lista[AL2] = AX1

# ______________________________________________________________________________________________________________________

def maior(lista: list, modo: int, iniciodalista: int = 0):  # Encontra o menor valor em uma lista
    if modo == 0:
        maiorElemento = lista[iniciodalista].get_nome()
    elif modo == 1:
        maiorElemento = int(lista[iniciodalista].get_valor())
    elif modo == 2:
        maiorElemento = float(lista[iniciodalista].get_força())
    elif modo == 3:
        maiorElemento = float(lista[iniciodalista].get_energia())
    posicaoMaiorElemento = iniciodalista
    tamanhoDaLista = len(lista)
    for contador in range(iniciodalista, tamanhoDaLista):
        if modo == 0 and lista[contador].get_nome() < maiorElemento:
            maiorElemento = lista[contador].get_nome()
            posicaoMaiorElemento = contador
        elif modo == 1 and int(lista[contador].get_valor()) < maiorElemento:
            maiorElemento = int(lista[contador].get_valor())
            posicaoMaiorElemento = contador
        elif modo == 2 and float(lista[contador].get_força()) < maiorElemento:
            maiorElemento = float(lista[contador].get_força())
            posicaoMaiorElemento = contador
        elif modo == 3 and float(lista[contador].get_energia()) < maiorElemento:
            maiorElemento = float(lista[contador].get_energia())
            posicaoMaiorElemento = contador
    return posicaoMaiorElemento

# ______________________________________________________________________________________________________________________

def ordenar(lista: list, modo: int):
    iniciodalista = 0
    fimdalista = len(lista) - 1
    while iniciodalista != fimdalista:
        maiorElemento = maior(lista, modo, iniciodalista)
        trocarDePosicao(lista, maiorElemento, iniciodalista)
        iniciodalista += 1
    fimdalista = len(lista) - 1
    iniciodalista = 0
    fimdalistaa = len(lista) - 1
    iniciodalistaa = 0

# ______________________________________________________________________________________________________________________

def embaralhar(lista: list):  #  Embaralha elementos de uma lista
    tamanhoDaLista = len(lista)
    T = tamanhoDaLista * 6
    for i in range(T):
        AL = randint(0, tamanhoDaLista - 1)
        AL2 = randint(0, tamanhoDaLista - 1)
        trocarDePosicao(lista, AL, AL2)

# ______________________________________________________________________________________________________________________

def lerArquivo(nome: str):  # Função para ler um arquivo e retornar seus dados numa lista
    arquivo = open(nome, 'r')
    aux = arquivo.readlines()
    arquivo.close()
    return aux

# ______________________________________________________________________________________________________________________

def separarDados(dadosDoArquivo: list):  # Separa informações contidas na mesma string 
    contarLetrasPalavra = 0
    matrizDadosArquivo: list = [] 
    Laux = [] 
    for contadorTamanhoDadosArquivo in range (len(dadosDoArquivo)):
        dadosDeUmCadastro: str = dadosDoArquivo[contadorTamanhoDadosArquivo]
        for letra in dadosDeUmCadastro:
            if letra != ';' and contarLetrasPalavra == 0:
                v = letra
            elif letra != ';' and letra != '\n' and contarLetrasPalavra != 0:
                v = v + letra
            elif letra == ';' and contarLetrasPalavra != 0:
                Laux.append(v)
                contarLetrasPalavra == -1
                v = ''  # 'apaga' a string para começar a armazenar novos caracteres
            elif letra == '\n':
                Laux.append(v)
                matrizDadosArquivo.append(deepcopy(Laux))
                Laux [:] = []
                contarLetrasPalavra = -1
            contarLetrasPalavra = contarLetrasPalavra + 1
            
    return matrizDadosArquivo
# ______________________________________________________________________________________________________________________

def comparar(a: Kard, b: Kard, tipoDeDisputa):
    if tipoDeDisputa == 1:  # Compara por valor
        if a.get_valor() > b.get_valor():
            return a
        elif a.get_valor() < b.get_valor():
            return b
        else:
            return 'empate'
    elif tipoDeDisputa == 2:  # Compara por força
        if a.get_força() > b.get_força():
            return a
        elif a.get_força() < b.get_força():
            return b
        else:
            return 'empate'
    elif tipoDeDisputa == 3:  # Compara por energia
        if a.get_energia() > b.get_energia():
            return a
        elif a.get_energia() < b.get_energia():
            return b
        else:
            return 'empate'
    elif tipoDeDisputa == 4:  # Compara por jokempo
        if a.get_jokempo() == 'Pedra' and b.get_jokempo() == 'Tesoura':
            return a
        elif a.get_jokempo()== 'Tesoura' and b.get_jokempo() == 'Pedra':
            return b
        elif a.get_jokempo() == 'Pedra' and b.get_jokempo() == 'Papel':
            return b
        elif a.get_jokempo() == 'Papel' and b.get_jokempo() == 'Pedra':
            return a
        elif a.get_jokempo() == 'Tesoura' and b.get_jokempo() == 'Papel':
            return a
        elif a.get_jokempo() == 'Papel' and b.get_jokempo() == 'Tesoura':
            return b
        elif a.get_jokempo() == b.get_jokempo():
            return 'empate'
# ______________________________________________________________________________________________________________________

def procurarJogador(players: list, nick: str):
    for player in range(len(players)):
        if players[player].get_nick() == nick:
            return player
    return None