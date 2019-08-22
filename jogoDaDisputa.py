Nickname = input('digite seu nome')

class Pilha():
    B = [] 
    def poe(self, m):
        self.B.insert(0, m)
    def tira(self):
        return self.B.pop(0) 

cartas = Pilha()

print(cartas.B)

cartas.poe(20)
cartas.poe('Daniel')

print(cartas.B)
cartas.poe('jilo')

print(cartas.tira())
