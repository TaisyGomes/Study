print('Bem-Vindo a Pizzaria da Taisy Gomes dos Santos') #RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS
print('----------------------Cardápio----------------------') #MENU
print('| Código | Descrição | Pizza Média | Pizza Grande  |')
print('|   21   | Napolitana|    R$ 20,00 |     R$ 26,00  |')
print('|   22   | Margherita|    R$ 20,00 |     R$ 26,00  |')
print('|   23   | Calabresa |    R$ 25,00 |     R$ 32,50  |')
print('|   24   | Toscana   |    R$ 30,00 |     R$ 39,00  |')
print('|   25   | Portuguesa|    R$ 30,00 |     R$ 39,00  |')
print('----------------------------------------------------')


sentinela = 1 #ajuda para parar o looping
acumulador = 0 #calcula valor total a pagar

while sentinela == 1 : 

    tamanho = input('Qual tamanho da pizza que deseja (M/G): ') #entrada para tamanho

    if tamanho != 'M' and tamanho != 'G': #verificando se digitou certo o tamanho
        print('Opção inválida!')
        continue

    codigo = int(input('Entre com o código do sabor desejado: ')) #entrada para codigo da pizza

    if codigo == 21: #validacao do codigo da pizza
        pizza = 'napolitana'
        if tamanho == 'M': 
            valor_pizza = 20
            acumulador+= valor_pizza #somador para total a ser pago
        else:
            valor_pizza = 26
            acumulador+= valor_pizza #somador para total a ser pago

    elif codigo == 22: #validacao do codigo da pizza
        pizza = 'margherita'
        if tamanho == 'M': 
            valor_pizza = 20
            acumulador+= valor_pizza #somador para total a ser pago
        else:
            valor_pizza = 26
            acumulador+= valor_pizza #somador para total a ser pago
    
    elif codigo == 23:  #validacao do codigo da pizza
        pizza = 'calabresa'
        if tamanho == 'M': 
            valor_pizza = 25
            acumulador+= valor_pizza #somador para total a ser pago
        else:
            valor_pizza = 32.50
            acumulador+= valor_pizza #somador para total a ser pago
    
    elif codigo == 24:  #validacao do codigo da pizza
        pizza = 'toscana'
        if tamanho == 'M': 
            valor_pizza = 30
            acumulador+= valor_pizza #somador para total a ser pago
        else:
            valor_pizza = 39
            acumulador+= valor_pizza #somador para total a ser pago
    
    elif codigo == 25:  #validacao do codigo da pizza
        pizza = 'portuguesa'
        if tamanho == 'M': 
            valor_pizza = 30
            acumulador+= valor_pizza #somador para total a ser pago
        else:
            valor_pizza = 39
            acumulador+= valor_pizza #somador para total a ser pago
    
    else: #caso a pessoa digite valor que nao corresponde a um codigo de pizza
        print('Opção inválida!')
        continue
    
    print('\nVocê pediu uma pizza de {}'.format(pizza)) #output da pizza escolhida
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    sentinela = int(input()) #verificando se ele quer mais pizza
    
    if sentinela == 0: break #caso ele nao queira o looping é interrompido

print('O valor a ser pago é: {:.2f}'.format(acumulador)) #valor a ser pago

#RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS
#codigo no git https://github.com/TaisyGomes/Study/tree/main/Uninter/DISCIPLINAS/LP/PRIMEIRO%20TRABALHO%20PR%C3%81TICO