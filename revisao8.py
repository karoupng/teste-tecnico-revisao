import json


def filtrar_clientes_vip(dados_usuario):
    clientes_vips = []
    for cliente in dados_usuario["usuarios"][0:]:
        status_vip = cliente.get("eh_vip", False)

        if status_vip:
            clientes_vips.append(cliente["nome"])

        else:
            print(f"{cliente['nome']} não é cliente vip")
            continue
    return clientes_vips


payload_marketing = '{"usuarios": [{"nome": "Ana", "eh_vip": true}, {"nome": "Carlos", "idade": 28}, {"nome": "Beatriz", "eh_vip": true}]}'

lista_clientes = json.loads(payload_marketing)

clientes_selo_vip = filtrar_clientes_vip(lista_clientes)

print(clientes_selo_vip)
