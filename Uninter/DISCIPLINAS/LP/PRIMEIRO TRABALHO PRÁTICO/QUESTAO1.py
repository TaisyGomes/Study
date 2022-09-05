print('Bem vindo a loja da Taisy Gomes dos Santos') #RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS
valor = float(input('Entre com o valor do produto: ')) # entrada para o valor do produto
quantidade = int(input('Entre com o valor da quantidade: ')) # entrada para quantidade do produto

if quantidade > 0:
    
    if 0 < quantidade <= 4:  # condição para execução de valores até 4 unidades
    
        total_sem_desconto = valor * quantidade
        print('O valor sem desconto foi: R$', total_sem_desconto)
        print('O valor com desconto foi: R$', total_sem_desconto, '(desconto 0%)')

    elif 5 <= quantidade <= 19:  # condição para execução de valores entre 5 e 19 unidades

        total_sem_desconto = valor * quantidade
        desconto = 0.03 * total_sem_desconto
        total_com_desconto = total_sem_desconto - desconto
        print('O valor sem desconto foi: R$', total_sem_desconto)
        print('O valor com desconto foi: R$', total_com_desconto, '(desconto 3%)')

    elif 20 <= quantidade <= 99: # condição para execução de valores entre 20 e 99 unidades

        total_sem_desconto = valor * quantidade
        desconto = 0.06 * total_sem_desconto
        total_com_desconto = total_sem_desconto - desconto
        print('O valor sem desconto foi: R$', total_sem_desconto)
        print('O valor com desconto foi: R$', total_com_desconto, '(desconto 6%)')

    else: # se a quantidade for igual ou maior que R$100, entra nesse else

        total_sem_desconto = valor * quantidade
        desconto = 0.1 * total_sem_desconto
        total_com_desconto = total_sem_desconto - desconto
        print('O valor sem desconto foi: R$', total_sem_desconto)
        print('O valor com desconto foi: R$', total_com_desconto, '(desconto 10%)')
else: # caso o usuário digite um valor inválido para a quantidade, entra nesse else
    print('Quantidade inválida, tente novamente!')

#RU IDENTIFICADOR 4232101 - TAISY GOMES DOS SANTOS