# Função para realizar o saque e atualizar o saldo
def realizar_saque(saldo, saque):
    if saldo >= saque:
        novo_saldo = saldo - saque
        return novo_saldo, "Saque realizado com sucesso. Novo saldo:", novo_saldo
    else:
        return saldo, "Saldo insuficiente. Saque nao realizado!"

# Função para exibir a mensagem formatada
def exibir_mensagem(mensagem):
    if len(mensagem) == 3:
        return f"{mensagem[1]} {mensagem[2]}"
    else:
        return mensagem[1]

# Entrada dos valores de saldo total e valor do saque
saldo_total = int(input())
valor_saque = int(input())

# Realiza o saque e obtém a mensagem apropriada
resultado_saque = realizar_saque(saldo_total, valor_saque)

# Exibe a mensagem formatada
mensagem_formatada = exibir_mensagem(resultado_saque)
print(mensagem_formatada)
