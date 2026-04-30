class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "1234"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    def ver_saldo(self):
        return self._saldo
        # print(f'Seu saldo é: {saldo}')

    def ver_numero(self):
        return self._numero
    
    def ver_agencia(self):
        return self._agencia
    
    def ver_cliente(self):
        return self._cliente
    
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

class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente) 
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self.valor):
        numero_saques = len(
            [Transacao for transacao in self._historico.transacoes if transação["tipo"] = Saque.__name__]
        )

        excedeu_limite = valor >self. limite
        excedeu_saques =numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou. Valor excede o limite")

        elif excedeu_saques:
            print('Operação falhou. Númeromáximode saques excedido.')

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''
            Agência: {self._agencia}
            C/c: {self._numero}
            Titular: {self._cliente.nome}
        '''
        
class Transacao:
    def valor(self):
        pass

    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transação = conta.sacar(self.valor)

        if sucesso_transação:
            conta.historico.adicionar_transacao(self)

class deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transação = conta.depositar(self.valor)

        if sucesso_transação:
            conta.historico.adicionar_transacao(self)

class Historico:
    historico = ["nome", "valor", "saque", "deposito"]



    def adicionar_transacao(self, nova_transacao):
        self._transacoes.append({
            "tipo":transacao.__class__.__name,
            "valor": transacao.valor,
        })
