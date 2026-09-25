def salvar_dados(clientes, contas, agencias):
    dados = [clientes, contas, agencias]

    arquivo = open("json.json", "w")
    json.dump(dados, arquivo, indent=4)
    arquivo.close()

    print("Dados salvos com sucesso!")


def depositar(contas):
    print("\n=== DEPÓSITO ===")

    numero = int(input("Número da conta: "))
    valor = float(input("Valor do depósito: R$ "))

    conta = procurar_conta(contas, numero)

    if conta == []:
        print("Conta não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        conta[3] = conta[3] + valor
        print("Depósito realizado com sucesso!")
        print("Novo saldo: R$", conta[3])


def sacar(contas):
    print("\n=== SAQUE ===")

    numero = int(input("Número da conta: "))
    valor = float(input("Valor do saque: R$ "))

    conta = procurar_conta(contas, numero)

    if conta == []:
        print("Conta não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    elif valor > conta[3]:
        print("Saldo insuficiente.")
    else:
        conta[3] = conta[3] - valor
        print("Saque realizado com sucesso!")
        print("Novo saldo: R$", conta[3])

def transferir(contas):
    print("\n=== TRANSFERÊNCIA ===")

    numero_origem = int(input("Conta de origem: "))
    numero_destino = int(input("Conta de destino: "))
    valor = float(input("Valor da transferência: R$ "))

    origem = procurar_conta(contas, numero_origem)
    destino = procurar_conta(contas, numero_destino)

    if origem == []:
        print("Conta de origem não encontrada.")
    elif destino == []:
        print("Conta de destino não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    elif valor > origem[3]:
        print("Saldo insuficiente.")
    else:
        origem[3] = origem[3] - valor
        destino[3] = destino[3] + valor

        print("Transferência realizada com sucesso!")


def consultar_saldo(contas):
    print("\n=== CONSULTAR SALDO ===")

    numero = int(input("Número da conta: "))

    conta = procurar_conta(contas, numero)

    if conta == []:
        print("Conta não encontrada.")
    else:
        print("Seu saldo atual é: R$", conta[3])
