class Produto:
    def __init__(self, nome, preco, stock):
        self._nome = nome
        self._preco = preco
        self._stock = stock

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def stock(self):
        return self._stock

