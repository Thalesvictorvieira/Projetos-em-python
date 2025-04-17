class Pessoa:
    def __init__(self, nome, idade, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura

irineu = Pessoa("Irineu",19,1.72)
print(irineu.idade)
print(irineu.nome)