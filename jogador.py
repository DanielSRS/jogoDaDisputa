class Jogador():
    def __init__(self, nick: str, partidasJogadas: int = 0, partidasVencidas: int = 0, taxaDeSucesso: float = 0.0):
        self.nick = nick
        self.partidasJogadas = partidasJogadas
        self.partidasVencidas = partidasVencidas
        self.taxaDeSucesso = taxaDeSucesso
    def get_nick(self):
        return self.nick
    def get_partidasJogadas(self):
        return self.partidasJogadas
    def get_partidasVencidas(self):
        return self.partidasVencidas
    def get_taxaDeSucesso(self):
        return self.taxaDeSucesso
    def adicionarPartida(self):
        self.partidasJogadas = self.partidasJogadas + 1
        self.taxaDeSucesso = self.get_partidasVencidas() * 100 / self.get_partidasJogadas()
    def adiconarVitorias(self):
        self.partidasVencidas = self.partidasVencidas + 1
        self.taxaDeSucesso = self.get_partidasVencidas() * 100 / self.get_partidasJogadas()
    def get_status(self):
        a = 'Nick: ' + self.get_nick()
        a += '\nQuantidade de partidas jogadas: ' + str(self.get_partidasJogadas())
        a += '\nQuantidade de partidas vencidas: ' + str(self.get_partidasVencidas())
        a += '\nTaxa de sucesso: ' + str(self.get_taxaDeSucesso()) + '%'
        return a
