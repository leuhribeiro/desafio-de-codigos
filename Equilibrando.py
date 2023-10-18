# Função para atualizar o saldo com base nas transações de depósito e retirada
def atualizar_saldo(saldo_atual, valor_deposito, valor_retirada):
    novo_saldo = saldo_atual + valor_deposito - valor_retirada
    return round(novo_saldo, 1)  # Arredonda o saldo para uma casa decimal

# Solicita a entrada do usuário
saldo_atual = float(input("Informe o saldo atual da conta: "))
valor_deposito = float(input("Informe o valor a ser depositado na conta: "))
valor_retirada = float(input("Informe o valor a ser retirado da conta: "))

# Chama a função para atualizar o saldo
novo_saldo = atualizar_saldo(saldo_atual, valor_deposito, valor_retirada)

# Exibe o saldo atualizado
print("Saldo atualizado: {:.1f}".format(novo_saldo))
