import datetime

class Product :
    def __init__(self, name, validity=None,price) -> None:
        self.nome = name
        self.validity = validity
        self.price = price

