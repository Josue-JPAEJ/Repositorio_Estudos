from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('================================================')
    print('============== Bem Vindo =======================')
    print('============== Geek Shop =======================')
    print('================================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto: ')
    print('2 - Listar Produto: ')
    print('3 - Comprar Produto: ')
    print('4 - Visualizar Carrinho: ')
    print('5 - Fechar Pedido: ')
    print('6 - Sair do Sistema: ')

    try:
        opcao: int = int(input())
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            visualizar_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('Volte Sempre!')
            sleep(2)
            exit(1)
    except:
        exit(1)


def cadastrar_produto() -> None:
    print('===========================')
    print('=== Cadastro de Produto ===')
    print('===========================')

    try:
        nome: str = str(input('Informe o nome do produto: '))
        preco: float = float(input('informe o preço do produto: '))

        produto: Produto = Produto(nome, preco)
        produtos.append(produto)

        print(f'O Produto "{produto.nome}" foi cadastrado com sucesso!')
        sleep(2)

    except:
        print('Dados Inválidos!')

    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('===========================')
        print('=== Listagem de Produto ===')
        print('===========================')

        for produto in produtos:
            print(produto)
            print('---------------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')

    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('===========================')
        print('=== Comprar de Produtos ===')
        print('===========================')
        print('')
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('==================== Produtos Disponíveis ====================')

        for produto in produtos:
            print(produto)
            print('---------------------------')
            sleep(1)
        try:
            codigo: int = int(input())
            produto: Produto = pega_produto_por_codigo(codigo)
            if produto:
                if len(carrinho) > 0:
                    tem_no_carrinho: bool = False
                    for item in carrinho:
                        quant: int = item.get(produto)
                        if quant:
                            item[produto] = quant + 1
                            print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho!')
                            tem_no_carrinho = True
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f'O Produto {produto.nome} foi adicionado ao carrinho.')
                else:
                    item = {produto: 1}
                    carrinho.append(item)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
            else:
                print(f'O produto com código {codigo} não foi encontrado.')
        except:
            print('Dados Inválidos!')
            sleep(2)
            menu()
    else:
        print('Nenhum produto cadastrado.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('===========================')
        print('======== Carrinho =========')
        print('===========================')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('---------------------------')
                sleep(1)
    else:
        print('Carrinho Vazio.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('===========================')
        print('======== Carrinho =========')
        print('===========================')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade : {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(2)

    else:
        print('Carrinho vazio.')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
