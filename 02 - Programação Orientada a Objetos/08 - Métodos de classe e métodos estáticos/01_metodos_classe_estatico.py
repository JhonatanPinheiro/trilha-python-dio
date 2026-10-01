class Pessoa:  # Define a classe Pessoa

    def __init__(self, nome, idade):  # Inicializa o objeto recebendo nome e idade
        self.nome = nome  # Armazena o nome da pessoa
        self.idade = idade  # Armazena a idade da pessoa

    @classmethod  # Define um método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):  # Cria uma Pessoa usando a data de nascimento
        idade = 2022 - ano  # Calcula a idade com base no ano de nascimento
        return cls(nome, idade)  # Cria e retorna um novo objeto Pessoa

    @staticmethod  # Define um método estático
    def e_maior_idade(idade):  # Recebe uma idade para verificar se é maior de idade
        return idade >= 18  # Retorna True se a idade for 18 ou mais


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")  # Cria uma Pessoa usando o método de classe
print(p.nome, p.idade)  # Mostra o nome e a idade da pessoa

print(Pessoa.e_maior_idade(18))  # Verifica se 18 anos é maior de idade
print(Pessoa.e_maior_idade(8))  # Verifica se 8 anos é maior de idade