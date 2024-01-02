from ItemPedido import ItemPedido


class Pedido:
    def __init__(self, codigo):
        self._codigo = codigo
        self._itens = []
        self._modo_pagamento = None

    @property
    def codigo(self):
        return self._codigo
    
    @property
    def modo_pagamento(self):
        return self._modo_pagamento
    
    @modo_pagamento.setter
    def modo_pagamento(self, modo_pagamento):
        self._modo_pagamento = modo_pagamento

    def adicionar_item(self, produto, quantidade):
        novo_item = ItemPedido(produto, quantidade)
        self._itens.append(novo_item)

    def mostrar_detalhes_item(self, item):
        print(f'     Produto: {item.produto.nome}')
        print(f'       Preço: {item.produto.preco:.2f} EURO')
        print(f'  Quantidade: {item.quantidade} UN')

    def listar_itens(self):
        self._itens.reverse()
        print(f' Ref. Pedido: {self._codigo}')
        for item in self._itens:
            print('  ------------------------')
            self.mostrar_detalhes_item(item)
    
    def calcular_total_pagar(self):
        total = 0
        for item in self._itens:
            total += item.quantidade * item.produto.preco
        return total