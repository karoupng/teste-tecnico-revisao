vendas_brutas = [
    "VND01|ELETRO|1500.00",
    "VND02|LIVROS|45.90",
    "VND03|ELETRO|350.00",
    "VND04|MODA|120.00",
    "VND05|LIVROS|89.90",
    "VND06|MODA|80.00",
]

faturamento_por_categoria = {}

for venda in vendas_brutas:
    codigo, categoria, valor = venda.split("|")

    # PASSO A: Converter o texto em número decimal (float)
    valor_decimal = float(valor)

    # PASSO B: Buscar o acumulado atual e somar o novo valor decimal
    faturamento_por_categoria[categoria] = (
        faturamento_por_categoria.get(categoria, 0.0) + valor_decimal
    )

# PASSO C: Fora do laço, imprimir o relatório final usando o .items()
print("=== RELATÓRIO DE FATURAMENTO ===")
for cat, total in faturamento_por_categoria.items():
    print(f"Categoria: {cat} | Total Faturado: R$ {total:.2f}")
