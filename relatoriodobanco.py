def relatorio_banco(clientes, contas, agencias):
    print("\n=== RELATÓRIO DO BANCO ===")

    print("Quantidade de clientes:", len(clientes))
    print("Quantidade de contas:", len(contas))
    print("Quantidade de agências:", len(agencias))

    print("\n=== MONTANTE DAS AGÊNCIAS ===")

    for agencia in agencias:
        numero_agencia = agencia[0]
        nome_agencia = agencia[1]
        montante = 0

        for conta in contas:
            if conta[2] == numero_agencia:
                montante = montante + conta[3]

        print("Agência:", numero_agencia)
        print("Nome:", nome_agencia)
        print("Montante: R$", montante)
        print("------------------------")

    montante_total = 0

    for conta in contas:
        montante_total = montante_total + conta[3]

    print("\n=== MONTANTE TOTAL DO BANCO ===")
    print("R$", montante_total)