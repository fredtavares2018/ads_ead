
valor = 1000
if valor <= 1830.29:
    valor -= valor * 0.08
elif valor <= 3050.52:
    valor -= valor * 0.09
elif valor <= 6101.06:
    valor -= valor * 0.11

print(valor)