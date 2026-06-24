import json

# O resultado esperado deve ser: {"Projeto Fênix": 13.0, "Projeto Alfa": 4.0}
payload_horas = '[{"projeto": "Projeto Fênix", "horas": 8.0}, {"projeto": "Projeto Alfa", "horas": 4.0}, {"projeto": "Projeto Fênix", "horas": 5.0}]'


def consolidar_horas_projetos(lista_apontamentos):
    relatorio_horas = {}
    for projeto in lista_apontamentos:
        nome_do_projeto = projeto["projeto"]
        valor_horas = projeto["horas"]

        if nome_do_projeto not in relatorio_horas:
            relatorio_horas[nome_do_projeto] = valor_horas
        else:
            relatorio_horas[nome_do_projeto] += valor_horas
    return relatorio_horas


json_horas = json.loads(payload_horas)
print(consolidar_horas_projetos(json_horas))
