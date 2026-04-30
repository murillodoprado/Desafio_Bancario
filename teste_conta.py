class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "1234"
        self._cliente = cliente
        # self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def ver_saldo(self):
        return self._saldo
        # print(f'Seu saldo é: {saldo}')

    @property
    def ver_numero(self):
        return self._numero
    
    @property
    def ver_agencia(self):
        return self._agencia
    
    @property
    def ver_cliente(self):
        return self._cliente
    
    @property
    def ver_historico(self):
        return self._historico

    def saque(self, valor_saque):
        saldo = self._saldo
        valor_saque = float(input("Qual valor quer sacar? "))

        if valor_saque > saldo:
            print("Falha. Você não tem saldo.")

        elif valor_saque == saldo:
            self._saldo == 0
            print("Sua conta agora está zerada.")

        else:
            self._saldo =- valor_saque
            print("Valor sacado com sucesso!")

    def deposito(self, valor_deposito):
        valor_deposito = float(input("Qual o valor do depósito?"))

        if valor_deposito > 0:
            self._saldo += valor_deposito
            print("Depósito realizado com sucesso!")

        else:
            print("O valor precisar ser maior que 0!")

conta = Conta(123, "Mu")
print(conta._cliente)
conta.deposito(2)
print(conta._saldo)

conta2 = Conta.nova_conta(12, "Allan")
conta2.deposito(2)
print(conta2._saldo)
print(conta2._cliente)

