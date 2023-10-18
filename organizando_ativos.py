# Recebe o número de ativos
num_ativos = int(input())

# Cria uma lista vazia para armazenar os ativos
ativos = []

# Recebe os ativos e os adiciona à lista
for i in range(num_ativos):
    ativo = input()
    ativos.append(ativo)

# Organiza a lista em ordem alfabética
ativos.sort()

# Exibe os ativos em ordem alfabética
for ativo in ativos:
    print(ativo)
