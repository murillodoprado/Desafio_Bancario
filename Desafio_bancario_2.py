
clientes = ["Mu"]

def main(self, clientes):    

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