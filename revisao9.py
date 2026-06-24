import json

# O desafio pede para retornar strings "Enviar" ou "Bloquear" e não acumularem lista externa
# Chaves OPCIONAIS em Json


def checar_envio_sms(dados_usuario):
    quer_sms = dados_usuario.get("receber_sms", False)
    if quer_sms:
        return "Enviar"

    else:
        return "Bloquear"


# Teste A: Usuário quer SMS (Deve retornar "Enviar")
usuario_A = '{"nome": "Ana", "receber_sms": true}'

# Teste B: Usuário comum, chave não existe (Deve retornar "Bloquear" de forma segura, sem KeyError)
usuario_B = '{"nome": "Carlos", "idade": 30}'


Lista_A = json.loads(usuario_A)
Lista_B = json.loads(usuario_B)


print(f"Resultado Ana: {checar_envio_sms(Lista_A)}")
print(f"Resultado Carlos: {checar_envio_sms(Lista_B)}")


# resultado = checar_envio_sms(Lista_A)
