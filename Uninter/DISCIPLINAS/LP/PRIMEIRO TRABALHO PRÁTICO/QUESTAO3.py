def volumeFeijoada(): #FUNCAO QUE PEDE O VOLUME DA FEIJOADA       RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS
    while True:
        print('Menu Volume Feijoada')

        try:
            volume = int(input('Entre com a quantidade que deseja(ml): ')) #ENTRADA DA QUANTIDADE
        except ValueError: 
            print('Digite o volume utilizando números.\n') #CASO DIGITE LETRAS E OUTROS SIMBOLOS
            continue
        
        if volume < 300 or volume > 5000: #VERIFICANDO SE O PEDIDO NÃO É ACEITO
            print('Não aceitamos porções menores que 300mL ou maiores que 5L. Tente novamente!')
            continue
        else:
            valor = volume * 0.08 #CALCULO DO VALOR A PAGAR PELO VOLUME
            break
    return valor #RETORNANDO O VALOR A SER PAGO

def opcaoFeijoada(): #FUNCAO QUE PEGA A OPCAO DE FEIJOADA
    while True:
        print('Menu opção feijoada') #MENU DE OPCOES
        print('Entre com a opção de Feijoada:')
        print('b - Básica (feijão + paiol + costelinha)')
        print('p - Premium (feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
        opcao = input() #ENTRADA PARA A OPCAO
        
        if opcao == 'b': #VERIFICACAO DA OPCAO
            multiplicador = 1.00 # MULTIPLICADOR PARA O VOLUME
            return multiplicador # RETORNO DO MULTIPLICADOR
        elif opcao == 'p': #VERIFICACAO DA OPCAO
            multiplicador = 1.25 # MULTIPLICADOR PARA O VOLUME
            return multiplicador # RETORNO DO MULTIPLICADOR
        elif opcao == 's': #VERIFICACAO DA OPCAO
            multiplicador = 1.50 # MULTIPLICADOR PARA O VOLUME
            return multiplicador # RETORNO DO MULTIPLICADOR
        else:
            print('Você não digitou uma opção válida')
            continue 

def acompanhamentoFeijoada(): #FUNCAO PARA O ACOMPANHAMENTO DA FEIJOADA
    acumulador = 0 #PARA CALCULAR O TOTAL A SER PAGO DE ACOMPANHAMENTO
    while True:
        print('Deseja mais algum acompanhamento:') #MENU DE ACOMPANHAMENTO
        print('0 - Não desejo mais acompanhamentos (Encerrar pedido)')
        print('1 - 200g de arroz')
        print('2 - 150g de farofa especial')
        print('3 - 100g de couve cozida')
        print('4 - 1 laranja descascada')
        opcao = input() #ENTRADA PARA O VALOR DO ACOMPANHAMENTO
         
        if opcao == '0': #VERIFICACAO DO ACOMPANHAMENTO
            return acumulador 
        elif opcao == '1': #VERIFICACAO DO ACOMPANHAMENTO
            acumulador += 5.00
        elif opcao == '2': #VERIFICACAO DO ACOMPANHAMENTO
            acumulador += 6.00
        elif opcao == '3': #VERIFICACAO DO ACOMPANHAMENTO
            acumulador += 7.00
        elif opcao == '4': #VERIFICACAO DO ACOMPANHAMENTO
            acumulador += 3.00
        else: #CASO DIGITE UM NUMERO INVALIDO
            print('Opção inválida')
            continue
      
print('Bem-Vindo ao Programa de Feijoada da Taisy Gomes dos Santos') #RU 4232101 - IDENTIFICADOR

valor = volumeFeijoada() #CHAMADA DA FUNCAO VOLUME FEIJOADA
multiplicador = opcaoFeijoada() #CHAMADA DA FUNCAO OPCAO FEIJOADA
acompanhamento = acompanhamentoFeijoada() #CHAMADA DA FUNCAO ACOMPANHAMENTO FEIJOADA

total = valor * multiplicador + acompanhamento #CALCULO DO TOTAL A SER PAGO
print('Valor a ser pago é: R${:.2f}(volume = {:.2f} * opção = {:.2f} + acompanhamento = {:.2f})'.format(total, valor, multiplicador, acompanhamento))

#OUTPUT DO TOTAL A SER PAGO PELO USUARIO (ACIMA)

#RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS