def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    # Calcula o valor final usando a fórmula de juros compostos
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    # Arredonda o valor final para duas casas decimais
    valor_final = round(valor_final, 2)
    return valor_final

# Solicita ao usuário que insira os valores
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

# Calcula o valor final e exibe o resultado
resultado = calcular_valor_final(valor_inicial, taxa_juros, periodo)
print("Valor final do investimento: R$", resultado)
