def listar_agencias(agencias):
    print("\n=== LISTA DE AGÊNCIAS ===")

    if len(agencias) == 0:
        print("Nenhuma agência cadastrada.")
    else:
        for agencia in agencias:
            print("Número:", agencia["numero"])
            print("Nome:", agencia["nome"])
            print("------------------------")


def procurar_agencia(agencias, numero):
    for agencia in agencias:
        if agencia["numero"] == numero:
            return agencia

    return {}