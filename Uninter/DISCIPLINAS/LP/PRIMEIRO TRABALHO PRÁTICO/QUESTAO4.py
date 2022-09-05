listaProdutos = [] #lista para armazenar os dicionarios     RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS

#Começo da função Cadastrar Produto
def cadastrarProduto(codigo_Produto):

    print('Você selecionou a opção de Cadastrar Produto')
    print('Código do produto {}'.format (codigo_Produto))
    produto = input('Por favor entre com o NOME do produto: ') #INPUT PARA NOME DO PRODUTO
    fabricante = input('Por favor entre com o FABRICANTE do produto: ') #INPUT PARA NOME DO FABRICANTE
    valor = int(input('Por favor entre com o VALOR (R$) do produto: ')) #INPUT PARA VALOR DO PRODUTO
    dicionarioProduto = {'codigo': codigo_Produto, 'produto': produto, 'fabricante': fabricante, 'valor': valor} #ARMAZENDO DADOS NO DICIONARIO
    listaProdutos.append(dicionarioProduto.copy()) #ADICIONANDO O DISCIONARIO NA LISTA
#Fim da função Cadastrar Produto   

#Começo da função Consultar Produto
def consultarProduto():
    while True:
        print('\nVocê selecionou a opção Consultar Produto ') #MENU DO CONSULTAR PRODUTOS
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos os Produtos ')
        print('2 - Consultar Produtos por Código')
        print('3 - Consultar Produtos por Fabricante')
        print('4 - Retornar')
        opcaoConsulta = input()

        if opcaoConsulta != '1' and opcaoConsulta != '2' and opcaoConsulta != '3' and opcaoConsulta != '4':
            print('Opção inválida. Tente novamente!') #CASO ELE DIGITE UMA OPCAO INVALIDA
            continue
        
        if opcaoConsulta == '1': #VERIFICANDO OPCAO
            for codigo in listaProdutos:
                for key, value in codigo.items():
                    print('{} : {}'.format(key, value))
                    
        elif opcaoConsulta == '2': #VERIFICANDO OPCAO
            codigo_escolhido = int(input('Digite o CÓDIGO do Produto: '))
            for codigo in listaProdutos:
                if codigo['codigo'] == codigo_escolhido:
                    for key, value in codigo.items():
                        print('{} : {}'.format(key, value))

        elif opcaoConsulta == '3': #VERIFICANDO OPCAO
            fabricante_escolhido = input('Digite o FABRICANTE do(s) Produto(s): ')
            for codigo in listaProdutos:
                if codigo['fabricante'] == fabricante_escolhido:
                    for key, value in codigo.items():
                        print('{} : {}'.format(key, value))
        else: #CASO EM QUE A OPCAO É 4 QUE É PARA RETORNAR
            break
#Fim da função Consultar Produto

#Começo da função Remover Produto
def removerProduto():
    print('Você selecionou a opção de Remover Produto')
    entrada = int(input('Digite o código do produto a ser removido: ')) #INPUT DO CODIGO DO PRODUTO A SER REMOVIDO
    for codigo in listaProdutos:
        if codigo['codigo'] == entrada:
            listaProdutos.remove(codigo) #REMOCAO DO PRODUTO
#Fim da função Remover Produto

contador = 0 #AUXILIA PARA IDENTIFICAR O PRODUTO, O CODIGO DELE
while True:
    
    print('\nBem vindo ao Controle de Estoque da Mercearia da Taisy Gomes dos Santos') #MENU PRINCIPAL
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Produto')
    print('2 - Consultar Produto (s)')
    print('3 - Remover Produto')
    print('4 - Sair')
    opcaoMenu = input() #INPUT DA OPCAO ESCOLHIDA NO MENU PRINCIPAL

    if opcaoMenu == '1': # VALIDACAO DA OPCAO
        contador+= 1
        cadastrarProduto(contador) #CHAMADA DA FUNCAO CADASTRAR PRODUTO
    elif opcaoMenu == '2': # VALIDACAO DA OPCAO
        consultarProduto() #CHAMADA DA FUNCAO CONSULTAR PRODUTO
    elif opcaoMenu == '3': # VALIDACAO DA OPCAO
        removerProduto() #CHAMADA DA FUNCAO REMOVER PRODUTO
    elif opcaoMenu == '4': # VALIDACAO DA OPCAO
        print('Atendimento encerrado.')
        break
    else: #CASO A OPCAO SEJA INVALIDA
        print('Opção inválida. Tente novamente!')
        continue

#RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS