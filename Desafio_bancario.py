class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transação(self, conta, transacao):
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
    def nova_conta(cls,cliente,numero):
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

class Transacao:

    
    def valor(self):
        pass

    def registrar(self, conta):
        pass

class Historico:
    historico = ["nome", "conta", "saque", "deposito"]



    def adicionar_transacao(self, nova_transacao):
        self.nova_transacao = nova_transacao





clientes = ["Murillo", "Allan"]
cliente = input('Informe seu nome: ')

if cliente not in clientes:
    print("Você ainda não é nosso cliente.")
        
else:
    print(f"Seja bem-vindo(a) {cliente}!")

menu_1 = """
    MENU:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>ESCOLHA UMA OPÇÃO: """

opcao = input(menu_1)