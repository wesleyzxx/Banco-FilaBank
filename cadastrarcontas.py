def listar_contas(contas):
    print("\n=== LISTA DE CONTAS ===")

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print("Número da conta:", conta["numero"])
            print("CPF do cliente:", conta["cpf"])
            print("Agência:", conta["agencia"])
            print("Tipo:", conta["tipo"])
            print("Saldo: R$", conta["saldo"])
            print("------------------------")


def procurar_conta(contas, numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta

    return {}

