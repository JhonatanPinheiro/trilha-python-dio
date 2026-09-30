lista = []  # Cria uma lista vazia

lista.append(1)  # Adiciona o número 1 ao final da lista
lista.append("Python")  # Adiciona a string "Python" ao final da lista
lista.append([40, 30, 20])  # Adiciona uma nova lista como elemento da lista principal
lista.append("Jhonatan")

print(lista)  # Exibe a lista completa: [1, "Python", [40, 30, 20]]

#Removendo todas as vogais do ultimo elemento da lista
print(lista[3].translate(str.maketrans("", "", "aiou")))
# Mostrando a lista completa, mas removendo as vogais apenas do último elemento na visualização
print(lista[:3] + [lista[3].translate(str.maketrans("", "", "aiou"))])
