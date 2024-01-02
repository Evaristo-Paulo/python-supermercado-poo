from Menu import menu_opcao, menu
from SuperMercado import kandando

while True:
    menu(kandando)
    opcao = input(' Informe a opção desejada: ')
    menu_opcao(opcao)
