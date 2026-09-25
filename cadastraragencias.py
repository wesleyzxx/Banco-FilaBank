def listar_agencias(agencias):
    print("\n=== LISTA DE AGÊNCIAS ===")

    if len(agencias) == 0:
        print("Nenhuma agência cadastrada.")
    else:
        for agencia in agencias:
            print("Número:", agencia[0])
            print("Nome:", agencia[1])
            print("------------------------")


def procurar_agencia(agencias, numero):
    for agencia in agencias:
        if agencia[0] == numero:
            return agencia

    return []