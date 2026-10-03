def validar_cpf(cpf):
    if len(cpf) != 11:
        return False

    if cpf.isnumeric() == False:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0

    for i in range(9):
        soma = soma + int(cpf[i]) * (10 - i)

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if digito1 != int(cpf[9]):
        return False

    soma = 0

    for i in range(10):
        soma = soma + int(cpf[i]) * (11 - i)

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito2 != int(cpf[10]):
        return False

    return True


def cadastrar_cliente(clientes):
    print("\n=== CADASTRO DE CLIENTE ===")

    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento: ")

    if validar_cpf(cpf) == False:
        print("CPF inválido.")
        return

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")