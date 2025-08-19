# Quanto devo pagar de imposto com base no salário anual
# Nesse código, está sendo testada a faixa salarial anual e aplicada a taxa correspondente
# Se a condição for verdadeira, ele aplica a taxa sobre o salário
# Caso contrário, segue para a próxima condição ou para o else

salario_anual = 45000
primeira_faixa = 9.70 / 100
segunda_faixa = 37.35 / 100
terceira_faixa = 49.50 / 100

if salario_anual <= 34712:
    valor_imposto = salario_anual * primeira_faixa
elif 34713 <= salario_anual <= 68507:
    valor_imposto = salario_anual * segunda_faixa
else:
    valor_imposto = salario_anual * terceira_faixa

print(f"Valor do imposto sobre o seu salário anual é: {valor_imposto:.2f}")
