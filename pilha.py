class Pilha():
    def __init__(self):
        self.B = []
    def poe(self, m):
        self.B.insert(0, m)
    def tira(self):
        return self.B.pop(0)
    def exibir(self):
        print(self.B)