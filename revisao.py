# ==============================================================================
# BLOCO 1: CRIAÇÃO, JUNÇÃO E EXTENSÃO DE LISTAS
# ==============================================================================

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]

# CONCATENAÇÃO (+): Cria uma TERCEIRA lista nova na memória. Mantém n1 e n2 intactas.
valores = n1 + n2
print("Lista concatenada (valores):", valores)

# EXTENSÃO (.extend): Modifica a lista original DIRETAMENTE, injetando os novos itens no fim.
n1.extend(n2)
print("Lista n1 estendida diretamente:", n1)


# ==============================================================================
# BLOCO 2: OPERAÇÕES DE CONSULTA, BUSCA E ESTATÍSTICA
# ==============================================================================

# TAMANHO, SOMA E EXTREMOS (Funções Nativas)
print("Quantidade de elementos (len):", len(valores))
print("Soma de todos os elementos (sum):", sum(valores))
print("Menor valor da lista (min):", min(valores))
print("Maior valor da lista (max):", max(valores))

# ORDENAÇÃO: sorted() gera uma NOVA lista ordenada sem alterar a original.
print("Lista ordenada crescente:", sorted(valores))
print("Lista ordenada decrescente:", sorted(valores, reverse=True))

# PERTENCIMENTO (in): Retorna True se o elemento existir na lista, ou False se não.
print("O número 12 está na lista?", 12 in valores)

# CONTAGEM (.count): Percorre a lista contando quantas vezes o elemento se repete.
print("Quantas vezes o número 0 aparece?", valores.count(0))

# LOCALIZAÇÃO (.index): Retorna a posição (índice) da PRIMEIRA ocorrência do elemento.
posicao_do_tres = valores.index(3)
print("O número 3 foi encontrado pela primeira vez no índice:", posicao_do_tres)


# ==============================================================================
# BLOCO 3: ALTERAÇÃO E MUTAÇÃO DE ELEMENTOS (INSERÇÃO E REMOÇÃO)
# ==============================================================================

# INCLUSÃO NO FINAL (.append): Empurra o valor para a última posição disponível.
valores.append(13)
print("Lista após .append(13):", valores)

# REMOÇÃO NO FINAL (.pop sem argumento): Remove e retorna o último elemento da lista.
valores.pop()
print("Lista após .pop() remover o último elemento:", valores)

# REMOÇÃO POR ÍNDICE (.pop com argumento): Remove o elemento daquela posição específica.
valores.pop(3)  # Remove quem estava no índice 3
print("Lista após .pop(3) remover o elemento do índice 3:", valores)

# INSERÇÃO EM POSIÇÃO ESPECÍFICA (.insert): Não substitui! Coloca o valor no índice e empurra os outros para a direita.
valores.insert(3, 21)  # Coloca o número 21 exatamente no índice 3
print("Lista após .insert(3, 21):", valores)


# ==============================================================================
# BLOCO 4: ENGENHARIA DE MEMÓRIA (CÓPIA VS REFERÊNCIA)
# ==============================================================================

# REFERÊNCIA DE PONTEIRO (Pegadinha de Teste Técnico):
# Ambas as variáveis apontam para o MESMO endereço de memória. Alterar lista_b altera valores!
lista_b = valores

# CLONAGEM REAL (.copy):
# Cria uma lista totalmente NOVA e independente na memória RAM. Alterar lista_segura NÃO afeta valores.
lista_segura = valores.copy()
