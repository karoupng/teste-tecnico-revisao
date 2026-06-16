# Dados do Cliente para Teste
cliente_score = 700
cliente_renda = 5500
cliente_negativado = False

# Dicionários de Características (Regras)
regras_black = {"score_minimo": 800, "renda_minima": 10000, "exige_limpo": True}
regras_gold = {"score_minimo": 650, "renda_minima": 5000}
regras_standard = {"score_minimo": 500, "renda_minima": 3000}

# Árvore de Decisão com Operadores Lógicos
# 1. Teste para o Cartão Black (Precisa de Score E Renda E histórico limpo)
if (
    cliente_score >= regras_black.get("score_minimo")
    and cliente_renda >= regras_black.get("renda_minima")
    and not cliente_negativado
):
    print("Cartão Aprovado: BLACK")

elif cliente_score >= regras_gold.get(
    "score_minimo"
) and cliente_renda >= regras_gold.get("renda_minima"):
    print("Cartão Aprovado: GOLD")
elif cliente_score >= regras_standard.get(
    "score_minimo"
) and cliente_renda >= regras_standard.get("renda_minima"):
    print("Cartão Aprovado : STANDARD")

# 4. Caso não atinja nenhum pré-requisito
else:
    print("Proposta de Crédito Recusada.")
