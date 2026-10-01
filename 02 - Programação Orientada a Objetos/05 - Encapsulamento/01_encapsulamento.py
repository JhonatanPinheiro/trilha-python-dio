class Conta:  # Define a classe Conta

    def __init__(self, nro_agencia, saldo=0):  # Cria o objeto recebendo a agência e o saldo
        self._saldo = saldo  # Guarda o saldo dentro do objeto
        self.nro_agencia = nro_agencia  # Guarda o número da agência dentro do objeto

    def depositar(self, valor):  # Define o método para depositar um valor
        # ...  # Indica que aqui poderia existir alguma outra lógica
        self._saldo += valor  # Adiciona o valor ao saldo atual

    def sacar(self, valor):  # Define o método para sacar um valor
        # ...  # Indica que aqui poderia existir alguma outra lógica
        self._saldo -= valor  # Diminui o valor do saldo atual

    def mostrar_saldo(self):  # Define o método para consultar o saldo
        # ...  # Indica que aqui poderia existir alguma outra lógica
        return self._saldo  # Retorna o saldo atual


conta = Conta("0001", 100)  # Cria um objeto Conta com agência "0001" e saldo inicial 100
conta.depositar(100)  # Adiciona 100 ao saldo da conta

print(conta.nro_agencia)  # Mostra o número da agência
print(conta.mostrar_saldo())  # Mostra o saldo atual da conta