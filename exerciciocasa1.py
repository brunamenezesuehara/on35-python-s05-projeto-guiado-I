def calcular_total_compra(items):
    total = 0
    codigo_10_count = 0

    for item in items:
        total += item['preco']
        if item['codigo'] == 10:
            codigo_10_count += 1

    if codigo_10_count > 1:
        for i, item in enumerate(items):
            if item['codigo'] == 10:
                if codigo_10_count > 1:
                    item['preco'] *= 0.5
                    codigo_10_count -= 1

 
    if total > 100:
        total *= 0.9

    return total


itens = [
    {'codigo': 10, 'preco': 50},
    {'codigo': 20, 'preco': 30},
    {'codigo': 10, 'preco': 40}
]

total_pago = calcular_total_compra(itens)
print(f"Total a ser pago: R${total_pago:.2f}")
