class Pessoa:  # Define a classe Pessoa

    def __init__(self, nome, ano_nascimento):  # Inicializa o objeto recebendo nome e ano de nascimento
        self.nome = nome  # Armazena o nome da pessoa
        self._ano_nascimento = ano_nascimento  # Armazena o ano de nascimento

    @property  # Permite acessar idade como se fosse um atributo
    def idade(self):  # Define o método que calcula a idade
        _ano_atual = 2022  # Define o ano atual usado no cálculo
        return _ano_atual - self._ano_nascimento  # Calcula e retorna a idade


pessoa = Pessoa("Guilherme", 1994)  # Cria um objeto Pessoa com nome e ano de nascimento
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")  # Mostra o nome e a idade da pessoa