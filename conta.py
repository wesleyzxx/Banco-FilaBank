def criar_conta(nome):
    print("=== CRIAÇÃO DA CONTA ===")
    print("Cliente:", nome)

    print("Conta criada com sucesso!")
    return 0


def consultar_saldo(saldo):
    print("Seu saldo atual é: R$", saldo)
    return saldo


def depositar(saldo, valor):
    if valor > 0:
        saldo = saldo + valor
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")

    return saldo


def sacar(saldo, valor):
    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo = saldo - valor
        print("Saque realizado com sucesso!")

    return saldo