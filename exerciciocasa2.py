def calcular_total_compra(items):
    total = 0
    codigo_10_count = 0

    for item in items:
        total += item['preco'] * item['quantidade']
        if item['codigo'] == 10:
            codigo_10_count += item['quantidade']

    if codigo_10_count > 1:
        count = 0
        for item in items:
            if item['codigo'] == 10:
                for _ in range(item['quantidade']):
                    count += 1
                    if count == 2:  
                        total -= item['preco'] * 0.5
                        break
    if total > 100:
        total *= 0.9

    return total

def alterar_quantidade(items, input_string):
    
    if input_string.startswith('x'):
        try:
            new_quantity = int(input_string[1:])
            item_index = int(input("Digite o índice do item que deseja alterar: "))
            items[item_index]['quantidade'] = new_quantity
        except (ValueError, IndexError):
            print("Entrada inválida. Certifique-se de que o índice e a quantidade são válidos.")
    return items
itens = [
    {'codigo': 10, 'preco': 50, 'quantidade': 1},
    {'codigo': 20, 'preco': 30, 'quantidade': 1},
    {'codigo': 10, 'preco': 40, 'quantidade': 1}
]
entrada = "x2"  
itens = alterar_quantidade(itens, entrada)

total_pago = calcular_total_compra(itens)
print(f"Total a ser pago: R${total_pago:.2f}")