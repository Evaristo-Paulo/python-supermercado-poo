from Pedido import Pedido


class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._pedido = None
        self._pedidos = []

    @property
    def pedido(self):
        return self._pedido
    
    @property
    def pedidos(self):
        return self._pedidos

    def iniciar_pedido(self, codigo_pedido):
        novo_pedido = Pedido(codigo_pedido)
        self._pedido = novo_pedido

    def concluir_pedido(self, modo_pagamento, valor):
        troco = valor - self._pedido.calcular_total_pagar()
        self._pedido.modo_pagamento = modo_pagamento
        self._pedidos.append(self._pedido)
        self._pedido = None
        return troco

    def listar_pedidos_concluidos(self):
        print('')
        self._pedidos.reverse()
        for pedido in self._pedidos:
            pedido.listar_itens()
            print('*******************')


cliente_generico = Cliente('John Doe')