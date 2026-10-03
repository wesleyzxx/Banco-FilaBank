def listar_clientes(clientes):
    print("\n=== LISTA DE CLIENTES ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print("Nome:", cliente["nome"])
            print("CPF:", cliente["cpf"])
            print("Data de nascimento:", cliente["data_nascimento"])
            print("------------------------")


def procurar_cliente(clientes, cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente

    return {}