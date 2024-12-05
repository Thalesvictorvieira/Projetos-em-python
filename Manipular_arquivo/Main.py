class Pessoa:
    def __init__(self,Nome,idade,altura) -> None:
        self.nome = Nome
        self.idade = idade
        self.altura = altura

irineu = Pessoa("Irineu",19,1.72)
print(irineu.idade)