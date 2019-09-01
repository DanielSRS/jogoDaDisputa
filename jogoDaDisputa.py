from copy import deepcopy
from random import randint


# ______________________________________________________________________________________________________________________
class Pilha():
    def __init__(self):
        self.B = []
    def poe(self, m):
        self.B.insert(0, m)
    def tira(self):
        return self.B.pop(0)
    def exibir(self):
        print(self.B)
# ______________________________________________________________________________________________________________________

class Kard():
    def __init__(self, nome: str, valor: int, força: float, energia: float, jokempo: str):
        self.nome = nome
        self.valor = valor
        self.força = força
        self.energia = energia
        self.jokempo = jokempo
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_força(self):
        return self.força
    def get_energia(self):
        return self.energia
    def get_jokempo(self):
        return self.jokempo


# ______________________________________________________________________________________________________________________

class Jogador():
    def __init__(self, nick: str, partidasJogadas: int = 0, partidasVencidas: float = 0.0):
        self.nick = nick
        self.partidasJogadas = partidasJogadas
        self.partidasVencidas = partidasVencidas
    def get_nome(self):
        return self.nick
    def get_partidasJogadas(self):
        return self.partidasJogadas
    def get_partidasVencidas(self):
        return self.partidasVencidas

# ______________________________________________________________________________________________________________________

def trocarDePosicao(lista: list, AL: int, AL2: int):  # Troca de posição dois elementos de uma lista
        AX1 = lista[AL]
        AX2 = lista[AL2]
        lista[AL] = AX2
        lista[AL2] = AX1

# ______________________________________________________________________________________________________________________

def maior(lista: list, iniciodalista: int = 0):  # Encontra o meior valor em uma lista (de numeros ao menos)
    maiorElemento = lista[iniciodalista]
    posicaoMaiorElemento = iniciodalista
    tamanhoDaLista = len(lista)
    for contador in range(iniciodalista, tamanhoDaLista):
        if lista[contador] > maiorElemento:
            maiorElemento = lista[contador]
            posicaoMaiorElemento = contador
    return posicaoMaiorElemento

# ______________________________________________________________________________________________________________________

def ordenar(lista: list):
    iniciodalista = 0
    fimdalista = len(lista) - 1
    while iniciodalista != fimdalista:
        maiorElemento = maior(lista, iniciodalista)
        trocarDePosicao(lista, maiorElemento, iniciodalista)
        #fimdalista -= 1
        iniciodalista += 1
    fimdalista = len(lista) - 1
    iniciodalista = 0
    fimdalistaa = len(lista) - 1
    iniciodalistaa = 0
    while not ( ((fimdalistaa + 1) % 2 == 0 and iniciodalista == fimdalista + 1) or ((fimdalistaa + 1) % 2 != 0 and iniciodalista == fimdalista) ):
        trocarDePosicao(lista, iniciodalista, fimdalista)
        iniciodalista += 1
        fimdalista -= 1

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

ckard = lerArquivo('./testes/Cartas.txt')  # usando diretorio de testes, para não modificar os arquivos

#  desagrupa os dados
ckard = separarDados(ckard)
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

Nickname = input('digite seu nome: ')

