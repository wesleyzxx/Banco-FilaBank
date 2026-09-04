from cliente import cadastrar_cliente
from conta import criar_conta, consultar_saldo, depositar, sacar


print("-------------------------------")
print("- BEM VINDO AO BANCO FILABANK -")
print("-------------------------------")


nome = cadastrar_cliente()

saldo = criar_conta(nome)

print("=== MENU ===")
print("1 - Consultar saldo")
print("2 - Depositar")
print("3 - Sacar")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    consultar_saldo(saldo)

elif opcao == "2":
    valor = float(input("Digite o valor do depósito: R$ "))
    saldo = depositar(saldo, valor)
    consultar_saldo(saldo)

elif opcao == "3":
    valor = float(input("Digite o valor do saque: R$ "))
    saldo = sacar(saldo, valor)
    consultar_saldo(saldo)

else:
    print("Opção inválida.")