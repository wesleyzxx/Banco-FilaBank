import json

from cadastrarcontas import procurar_conta


def salvar_dados(clientes, contas, agencias):
    dados = {
        "clientes": clientes,
        "contas": contas,
        "agencias": agencias
    }

    arquivo = open("json.json", "w")
    json.dump(dados, arquivo, indent=4)
    arquivo.close()

    print("Dados salvos com sucesso!")


def depositar(contas):
    print("\n=== DEPÓSITO ===")

    numero = int(input("Número da conta: "))
    valor = float(input("Valor do depósito: R$ "))

    conta = procurar_conta(contas, numero)

    if conta == {}:
        print("Conta não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        conta["saldo"] = conta["saldo"] + valor

        print("Depósito realizado com sucesso!")
        print("Novo saldo: R$", conta["saldo"])


def sacar(contas):
    print("\n=== SAQUE ===")

    numero = int(input("Número da conta: "))
    valor = float(input("Valor do saque: R$ "))

    conta = procurar_conta(contas, numero)

    if conta == {}:
        print("Conta não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    else:
        conta["saldo"] = conta["saldo"] - valor

        print("Saque realizado com sucesso!")
        print("Novo saldo: R$", conta["saldo"])


def transferir(contas):
    print("\n=== TRANSFERÊNCIA ===")

    numero_origem = int(input("Conta de origem: "))
    numero_destino = int(input("Conta de destino: "))
    valor = float(input("Valor da transferência: R$ "))

    origem = procurar_conta(contas, numero_origem)
    destino = procurar_conta(contas, numero_destino)

    if origem == {}:
        print("Conta de origem não encontrada.")
    elif destino == {}:
        print("Conta de destino não encontrada.")
    elif valor <= 0:
        print("Valor inválido.")
    elif valor > origem["saldo"]:
        print("Saldo insuficiente.")
    else:
        origem["saldo"] = origem["saldo"] - valor
        destino["saldo"] = destino["saldo"] + valor

        print("Transferência realizada com sucesso!")


def consultar_saldo(contas):
    print("\n=== CONSULTAR SALDO ===")

    numero = int(input("Número da conta: "))

    conta = procurar_conta(contas, numero)

    if conta == {}:
        print("Conta não encontrada.")
    else:
        print("Número da conta:", conta["numero"])
        print("Tipo:", conta["tipo"])
        print("Saldo atual: R$", conta["saldo"])