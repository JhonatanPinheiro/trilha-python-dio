def somar(a, b):  # Define uma função que recebe dois números

    return a + b  # Soma os dois números e retorna o resultado


def exibir_resultado(a, b, funcao):  # Define uma função que recebe dois números e outra função

    resultado = funcao(a, b)  # Executa a função recebida passando a e b como argumentos

    print(f"O resultado da operação {a} + {b} = {resultado}")  # Exibe o resultado da operação


exibir_resultado(10, 10, somar)  # Passa 10, 10 e a função somar como argumentos → O resultado da operação 10 + 10 = 20

# Observação: em Python, funções podem ser passadas como argumentos para outras funções.