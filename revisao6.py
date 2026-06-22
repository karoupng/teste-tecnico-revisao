import json


def listar_produtos_criticos(dados):

    produtos_criticos = []

    try:
        produtos = dados["inventario"]
    except KeyError:
        print("A chave não foi encontrada!")

    for produto in produtos:
        try:
            if produto["quantidade"] < 10:
                produtos_criticos.append(produto["produto"])
        except TypeError:
            print("Tipo inválido")
            continue

    return produtos_criticos


payload_estoque = '{"galpao": "Matriz", "inventario": [{"produto": "Teclado", "quantidade": 5}, {"produto": "Mouse", "quantidade": 15}, {"produto": "Monitor", "quantidade": 3}]}'
payload_2 = '{"galpao": "Matriz"}'


estoque = json.loads(payload_estoque)
payload_dois = json.loads(payload_2)


listar_payload_A = listar_produtos_criticos(estoque)
listar_payload_B = listar_produtos_criticos(payload_2)

print(f"Produtos críticos com pouco estoque:  {listar_payload_A}")
print(f"Mensagem Payload 2: {listar_payload_B}")
