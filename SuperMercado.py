class SuperMercado:
    def __init__(self, nome):
        self._nome = nome
        self._produtos = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def produtos(self):
        return self._produtos
    
    def dar_entrada_produto(self, produto):
        self._produtos.append(produto)

    def mostrar_detalhes_produto(self, produto):
        print(f'Produto: {produto.nome}')
        print(f'  Preço: {produto.preco:.2f} EURO')
        print(f'  Stock: {produto.stock} UN')

    def mostrar_detalhes_cliente(self, cliente):
        print(f'  Nome: {cliente.nome}')

    def listar_produto(self):
        self._produtos.reverse()
        for produto in self._produtos:
            self.mostrar_detalhes_produto(produto)
            print('')

    def buscar_produto(self, pesquisa: str):
        for produto in self._produtos:
            if produto.nome.lower() == pesquisa.lower():
                return produto
        return None


kandando = SuperMercado('Kandando')
