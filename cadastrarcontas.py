def listar_contas(contas):
    print("\n=== LISTA DE CONTAS ===")

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print("Número da conta:", conta[0])
            print("CPF do cliente:", conta[1])
            print("Agência:", conta[2])
            print("Saldo: R$", conta[3])
            print("------------------------")

def procurar_conta(contas, numero):
    for conta in contas:
        if conta[0] == numero:
            return conta

    return []

