import json


def calcular_total_vendas(dados):
    total_vendas = 0.0

    if "lista_vendas" in dados:
        vendas = dados["lista_vendas"]
        for venda in vendas:
            total_vendas += venda
    elif "historico_vendas" in dados:
        vendas = dados["historico_vendas"]
        for venda in vendas:
            total_vendas += venda
    else:
        return 0.0

    return total_vendas


payload_antigo = '{"loja": "Sul", "lista_vendas": [100.0, 250.0, 50.0]}'

# Teste 2 (Sistema Novo)
payload_novo = '{"loja": "Norte", "historico_vendas": [300.0, 150.0]}'

# Teste 3 (JSON com defeito/formato desconhecido - deve retornar 0.0)
payload_invalido = '{"loja": "Oeste", "dados_perdidos": [10.0]}'


dados_antigos = json.loads(payload_antigo)
dados_novos = json.loads(payload_novo)

calculo_total = calcular_total_vendas(dados_novos)

print(calculo_total)


payload_antigo = '{"loja": "Sul", "lista_vendas": [100.0, 250.0, 50.0]}'

# Teste 2 (Sistema Novo)
payload_novo = '{"loja": "Norte", "historico_vendas": [300.0, 150.0]}'

# Teste 3 (JSON com defeito/formato desconhecido - deve retornar 0.0)
payload_invalido = '{"loja": "Oeste", "dados_perdidos": [10.0]}'


dado_antigo = json.loads(payload_antigo)
dado_novo = json.loads(payload_novo)

calculo = calcular_total_vendas(dado_antigo)
print(dado_antigo)
