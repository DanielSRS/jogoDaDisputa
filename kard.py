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
    def get_carta(self):
        a = self.get_nome() + ', Valor: ' + self.get_valor() + ', Força: ' + self.get_força() + ', Energia: ' + self.get_energia()
        a = a + ', Jokempô: ' + self.get_jokempo()
        return a