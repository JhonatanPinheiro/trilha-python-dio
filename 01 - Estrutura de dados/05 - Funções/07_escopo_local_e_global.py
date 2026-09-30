salario = 2000  # Cria uma variável global com o valor inicial do salário


def salario_bonus(bonus):  # Define uma função que recebe o valor do bônus

    global salario  # Permite alterar dentro da função a variável global salario

    salario += bonus  # Adiciona o bônus ao salário atual

    return salario  # Retorna o novo valor do salário


salario_bonus(500)  # Adiciona 500 ao salário → 2500

# Observação: global permite que a função altere diretamente a variável salario que foi criada fora da função.