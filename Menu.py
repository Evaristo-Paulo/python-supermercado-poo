from os import system
from random import randint
from Produto import Produto
from Cliente import cliente_generico
from SuperMercado import kandando


def msg_erro(mensagem):
    print(f' ERRO: Não conseguimos localizar {mensagem}')


def limpar_tela():
    print()
    input("Por favor, digite 'Enter' para voltar ao 'Menu inicial'")
    system('cls')


def menu(supermercado):
    print(f'   Super mercado {supermercado.nome}')
    print(' 1 | Registar produto')
    print(' 2 | Listar produtos')
    print(' 3 | Buscar produto')
    print(' 4 | Adicionar item ao pedido')
    print(' 5 | Listar itens do pedido')
    print(' 6 | Efectuar pagamento')
    print(' 7 | Ver histórico de cliente')
    print(' 0 | Sair')
    print()


def menu_opcao(opcao):
    print('')
    if opcao == '1':
        print(' Registar produto')
        nome = input('  Produto: ')
        preco = input('    Preço: ')
        stock = input('    stock: ')

        float_preco = float(preco)
        int_stock = float(stock)

        novo_produto = Produto(nome, float_preco, int_stock)
        kandando.dar_entrada_produto(novo_produto)
        # LISTAR PRODUTOS NO SUPERMERCADO
        print('')
        kandando.listar_produto()
    elif opcao == '2':
        print(' Listar produtos')
        if len(kandando.produtos) > 0:
            kandando.listar_produto()
        else:
            print(' - Não há produtos registrados.')
    elif opcao == '3':
        print(' Buscar produto')
        nome = input('  Produto: ')
        print('')
        produto = kandando.buscar_produto(nome)

        if produto is not None:
            kandando.mostrar_detalhes_produto(produto)
        else:
            texto = f'o produto \'{nome}\''
            msg_erro(texto)
    elif opcao == '4':
        print(' Adicionar item ao pedido')
        nome = input('      Produto: ')
        quantidade = input('   Quantidade: ')
        print('')
        produto = kandando.buscar_produto(nome)
        if produto is not None:
            int_quantidade = int(quantidade)
            # VERIFICAR SE AINDA NÃO TEM PEDIDO
            if cliente_generico.pedido is None:
                cod_pedido = randint(2024, 5000) # GERA CÓDIGO PEDIDO ALEATÓRIO
                cliente_generico.iniciar_pedido(cod_pedido)
            
            cliente_generico.pedido.adicionar_item(produto, int_quantidade)
            cliente_generico.pedido.listar_itens()
        else:
            texto = f'o produto {nome}'
            msg_erro(texto)
    elif opcao == '5':
        print(' Listar itens do pedido')
        if cliente_generico.pedido is not None:
            cliente_generico.pedido.listar_itens()
        else:
            print(' - Não há pedido disponível.')
    elif opcao == '6':
        print(' Efectuar pagamento')
        if cliente_generico.pedido is not None:
            total = cliente_generico.pedido.calcular_total_pagar()
            cliente_generico.pedido.listar_itens()
            print('')
            print(f' Total a pagar: {total:.2f} EURO')
            modo_pagamento = input('Modo de pagamento: ')
            valor_pago = input('Valor (EURO): ')
            float_valor_pago = float(valor_pago)
            print('-----------------------------')
            if float_valor_pago >= total:
                troco = cliente_generico.concluir_pedido(modo_pagamento, float_valor_pago)
                if troco > 0:
                    print(f' - Seu troco é de {troco:.2f} EURO.')
            else:
                print(f' - Informe um valor superior ou igual a {total}')
        else:
            print(' - Não há pedido disponível.')
    elif opcao == '7':
        print(' Ver histórico de cliente')
        if len(cliente_generico.pedidos) > 0:
            cliente_generico.listar_pedidos_concluidos()
        else:
            print(' - Não há pedidos concluídos.')
    elif opcao == '0':
        return
    else:
        msg_erro('esta opção.')

    limpar_tela()