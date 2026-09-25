from cliente import cadastrar_cliente

def listar_clientes(clientes):
    print("\n=== LISTA DE CLIENTES ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print("Nome:", cliente[0])
            print("CPF:", cliente[1])
            print("Data de nascimento:", cliente[2])
            print("------------------------")


def procurar_cliente(clientes, cpf):
    for cliente in clientes:
        if cliente[1] == cpf:
            return cliente

    return []