def precoRoupa():
    valor = float(input("Digite o valor do produto: "))
    desconto = 0

    if valor <= 1830.29:                    #comparacao
        desconto = valor - valor * 0.08     # 1000 - 1000 x 8% = 920
    elif valor <= 3050.52:         
        desconto = valor - valor * 0.09
    elif valor <= 6101.06:
        desconto = valor - valor * 0.11

    print('Valor a ser pago ',desconto)
    desc_val = valor - desconto
    print('Desconto ',desc_val)

precoRoupa()

