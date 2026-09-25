def cadastrar_cliente(clientes):
    print("\n=== CADASTRO DE CLIENTE ===")

    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento: ")

    cliente = [nome, cpf, data_nascimento]
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")