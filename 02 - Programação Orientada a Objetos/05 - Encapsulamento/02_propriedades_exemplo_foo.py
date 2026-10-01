class Foo:  # Define a classe Foo

    def __init__(self, x=None):  # Inicializa o objeto recebendo x, que por padrão é None
        self._x = x  # Armazena o valor de x no atributo _x

    @property  # Permite acessar x como se fosse um atributo
    def x(self):  # Define o método para consultar o valor de x
        return self._x or 0  # Retorna _x; se _x for None ou outro valor considerado falso, retorna 0

    @x.setter  # Define o que acontece quando atribuímos um valor para x
    def x(self, value):  # Recebe o valor que será atribuído a x
        self._x += value  # Adiciona o valor recebido ao valor atual de _x

    @x.deleter  # Define o que acontece quando usamos del foo.x
    def x(self):  # Define o método executado ao deletar x
        self._x = 0  # Define _x como 0


foo = Foo(10)  # Cria um objeto Foo com _x começando em 10
print(foo.x)  # Acessa x através da propriedade e mostra 10

del foo.x  # Executa o deleter e define _x como 0
print(foo.x)  # Acessa x e mostra 0

foo.x = 10  # Executa o setter e adiciona 10 ao _x
print(foo.x)  # Acessa x e mostra 10