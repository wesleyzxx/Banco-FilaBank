def criar_conta(contas, clientes, agencias):
    print("\n=== CRIAÇÃO DE CONTA ===")

    cpf = input("CPF do cliente: ")

    cliente = procurar_cliente(clientes, cpf)

    if cliente == []:
        print("Cliente não encontrado.")
        return

    numero_agencia = int(input("Número da agência: "))

    agencia = procurar_agencia(agencias, numero_agencia)

    if agencia == []:
        print("Agência não encontrada.")
        return

    numero_conta = len(contas) + 1

    conta = [numero_conta, cpf, numero_agencia, 0]
    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Número da conta:", numero_conta)
