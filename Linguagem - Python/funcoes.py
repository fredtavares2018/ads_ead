def precoRoupa():
    valor = 3100
    if valor <= 1830.29:          #comparacao
        valor -= valor * 0.08     # 1000 - 1000 x 8% = 920
    elif valor <= 3050.52:         
        valor -= valor * 0.09     # 2000 - 2000 x 9% = 1820
    elif valor <= 6101.06:
        valor -= valor * 0.11
        
    print(valor)

precoRoupa()
        
# valor - desconto = valor com desconto