#Tuplas sao estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses!
frutas = (                         # Cria uma tupla chamada frutas
    "laranja",                     # Primeiro elemento da tupla
    "pera",                        # Segundo elemento da tupla
    "uva",                         # Terceiro elemento da tupla
)

print(frutas)                      # Exibe a tupla completa


letras = tuple("python")           # Converte cada caractere de "python" em um elemento da tupla

print(letras)                      # Exibe a tupla de letras


numeros = tuple([1, 2, 3, 4])      # Converte a lista [1, 2, 3, 4] em uma tupla

print(numeros)                     # Exibe a tupla de números


pais = ("Brasil",)                 # Cria uma tupla com apenas um elemento
                                   # A vírgula é necessária para indicar que é uma tupla

print(pais)                        # Exibe a tupla