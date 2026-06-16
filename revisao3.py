# Dados do objeto Cadastrado
mala_peso = 35
mala_comprimento = 120
mala_liquidos = True

regras_especial = {
    "peso_ideal": 32,
    "comp_ideal": 150,
}

regras_inspecao = {
    "contem_liquidos": True,
    "peso_ideal": 23,
}

regras_padrao = {"peso_min": 10, "peso_max": 23}

regras_bagagem_mao = {"contem_liquidos": False, "peso_ideal": 10}

if mala_peso > regras_especial.get(
    "peso_ideal"
) or mala_comprimento > regras_especial.get("comp_ideal"):
    print("Sua mala vai para o despacho especial!")
elif mala_liquidos and mala_peso > regras_inspecao.get("peso_ideal"):
    print("Sua mala vai para inspeção!")
elif mala_peso > regras_padrao.get("peso_min") and mala_peso <= regras_padrao.get(
    "peso_max"
):
    print("Sua mala vai para o despacho padrão!")
else:
    print("Sua mala é uma bagagem de mão.")
