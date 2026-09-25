def cadastrar_agencia(agencias):
    print("\n=== CADASTRO DE AGÊNCIA ===")

    numero = int(input("Número da agência: "))
    nome = input("Nome da agência: ")

    agencia = [numero, nome]
    agencias.append(agencia)

    print("Agência cadastrada com sucesso!")