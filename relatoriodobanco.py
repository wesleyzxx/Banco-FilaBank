def relatorio_banco(clientes, contas, agencias):
    print("\n=== RELATÓRIO DO BANCO ===")

    print("Quantidade de clientes:", len(clientes))
    print("Quantidade de contas:", len(contas))
    print("Quantidade de agências:", len(agencias))

    print("\n=== MONTANTE POR AGÊNCIA ===")

    for agencia in agencias:
        numero_agencia = agencia["numero"]
        montante = 0

        for conta in contas:
            if conta["agencia"] == numero_agencia:
                montante = montante + conta["saldo"]

        print("Agência:", agencia["numero"])
        print("Nome:", agencia["nome"])
        print("Montante: R$", montante)
        print("------------------------")

    montante_total = 0

    for conta in contas:
        montante_total = montante_total + conta["saldo"]

    print("\n=== MONTANTE TOTAL DO BANCO ===")
    print("R$", montante_total)