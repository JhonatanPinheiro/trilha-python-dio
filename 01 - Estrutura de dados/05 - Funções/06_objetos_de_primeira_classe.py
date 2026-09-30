#Funcao de Somar
def somar(a, b):  # Define uma função que recebe dois números
    return a + b  # Soma os dois números e retorna o resultado

#Funcao de Subtracao
def subtrair(a, b):  # Define uma função que recebe dois números
    
    return a - b  # Soma os dois números e retorna o resultado

#Funcao de Multiplicacao
def multiplicacao(a,b):
    return a * b

#Funcao de Divisão
def divisao(a,b):
    return a / b

# Funcao para Exibir o Resultado
def exibir_resultado(a, b, funcao):  # Define uma função que recebe dois números e outra função
    resultado = funcao(a, b)  # Executa a função recebida passando a e b como argumentos
    print(f"O resultado da operação {a} + {b} = {resultado}")  # Exibe o resultado da operação


exibir_resultado(10, 10, somar)  # Passa 10, 10 e a função somar como argumentos → O resultado da operação 10 + 10 = 20
exibir_resultado(10,10,subtrair) # Passa 10, 10 e a função somar como argumentos → O resultado da operação 10 - 10 = 20
exibir_resultado(10, 10, multiplicacao)  # Passa 10, 10 e a função somar como argumentos → O resultado da operação 10 * 10 = 100
exibir_resultado(10,10,divisao) # Passa 10, 10 e a função somar como argumentos → O resultado da operação 10 / 10 = 1

# Atriuindo a funcao para uma variavel
variavel_exibir_resultado = exibir_resultado
print(variavel_exibir_resultado(4,24,multiplicacao))

# Observação: em Python, funções podem ser passadas como argumentos para outras funções.