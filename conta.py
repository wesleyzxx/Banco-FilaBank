def criar_conta(contas, clientes, agencias):
    print("\n=== CRIAÇÃO DE CONTA ===")

    cpf = input("CPF do cliente: ")

    cliente = procurar_cliente(clientes, cpf)

    if cliente == {}:
        print("Cliente não encontrado.")
        return

    numero_agencia = int(input("Número da agência: "))

    agencia = procurar_agencia(agencias, numero_agencia)

    if agencia == {}:
        print("Agência não encontrada.")
        return

    print("\n=== TIPO DE CONTA ===")
    print("1 - Salário")
    print("2 - Corrente")
    print("3 - Poupança")

    opcao = input("Escolha o tipo de conta: ")

    if opcao == "1":
        tipo = "salário"
    elif opcao == "2":
        tipo = "corrente"
    elif opcao == "3":
        tipo = "poupança"
    else:
        print("Opção inválida.")
        return

    numero_conta = len(contas) + 1

    conta = {
        "numero": numero_conta,
        "cpf": cpf,
        "agencia": numero_agencia,
        "tipo": tipo,
        "saldo": 0
    }

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Número da conta:", numero_conta)
    print("Tipo:", tipo)


def procurar_cliente(clientes, cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente

    return {}


def procurar_agencia(agencias, numero):
    for agencia in agencias:
        if agencia["numero"] == numero:
            return agencia

    return {}
