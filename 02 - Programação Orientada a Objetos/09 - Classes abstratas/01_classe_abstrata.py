from abc import ABC, abstractmethod, abstractproperty  # Importa recursos para criar classes e métodos abstratos


class ControleRemoto(ABC):  # Define uma classe abstrata chamada ControleRemoto

    @abstractmethod  # Define ligar como um método obrigatório nas classes filhas
    def ligar(self):  # Define o método ligar
        pass  # Não possui implementação aqui

    @abstractmethod  # Define desligar como um método obrigatório nas classes filhas
    def desligar(self):  # Define o método desligar
        pass  # Não possui implementação aqui

    @property  # Permite acessar marca como uma propriedade
    @abstractproperty  # Define marca como uma propriedade abstrata
    def marca(self):  # Define a propriedade marca
        pass  # Não possui implementação aqui


class ControleTV(ControleRemoto):  # Define ControleTV herdando de ControleRemoto

    def ligar(self):  # Implementa o método ligar
        print("Ligando a TV...")  # Mostra a mensagem de ligação
        print("Ligada!")  # Mostra que a TV foi ligada

    def desligar(self):  # Implementa o método desligar
        print("Desligando a TV...")  # Mostra a mensagem de desligamento
        print("Desligada!")  # Mostra que a TV foi desligada

    @property  # Permite acessar marca como uma propriedade
    def marca(self):  # Implementa a propriedade marca
        return "Philco"  # Retorna a marca da TV


class ControleArCondicionado(ControleRemoto):  # Define ControleArCondicionado herdando de ControleRemoto

    def ligar(self):  # Implementa o método ligar
        print("Ligando o Ar Condicionado...")  # Mostra a mensagem de ligação
        print("Ligado!")  # Mostra que o ar-condicionado foi ligado

    def desligar(self):  # Implementa o método desligar
        print("Desligando o Ar Condicionado...")  # Mostra a mensagem de desligamento
        print("Desligado!")  # Mostra que o ar-condicionado foi desligado

    @property  # Permite acessar marca como uma propriedade
    def marca(self):  # Implementa a propriedade marca
        return "LG"  # Retorna a marca do ar-condicionado


controle = ControleTV()  # Cria um objeto ControleTV
controle.ligar()  # Chama o método para ligar a TV
controle.desligar()  # Chama o método para desligar a TV
print(controle.marca)  # Mostra a marca da TV


controle = ControleArCondicionado()  # Cria um objeto ControleArCondicionado
controle.ligar()  # Chama o método para ligar o ar-condicionado
controle.desligar()  # Chama o método para desligar o ar-condicionado
print(controle.marca)  # Mostra a marca do ar-condicionado