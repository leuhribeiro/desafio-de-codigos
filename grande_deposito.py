saldo = 0.0

valor = float(input("Digite o valor do depósito: "))

if valor > 0:
    saldo += valor
    print("Depósito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor inválido! Digite um valor maior que zero.")
