import json

from cliente import cadastrar_cliente
from conta import criar_conta
from agencia import cadastrar_agencia
from cadastrarclientes import listar_clientes, procurar_cliente
from cadastrarcontas import listar_contas, procurar_conta
from cadastraragencias import listar_agencias, procurar_agencia
from relatoriodobanco import relatorio_banco

def carregar_dados():
    try:
        arquivo = open("json.json", "r")
        dados = json.load(arquivo)
        arquivo.close()

        return dados

    except:
        return [[], [], []]


clientes = []
contas = []
agencias = []

dados = carregar_dados()

clientes = dados[0]
contas = dados[1]
agencias = dados[2]


opcao = ""

while opcao != "0":

    print("\n================================")
    print("       BANCO FILABANK")
    print("================================")

    print("1 - Cadastrar cliente")
    print("2 - Cadastrar conta")
    print("3 - Cadastrar agência")
    print("4 - Listar clientes")
    print("5 - Listar contas")
    print("6 - Listar agências")
    print("7 - Sacar")
    print("8 - Transferir")
    print("9 - Depositar")
    print("10 - Consultar saldo")
    print("11 - Relatório do banco")
    print("12 - Salvar dados")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente(clientes)

    elif opcao == "2":
        criar_conta(contas, clientes, agencias)

    elif opcao == "3":
        cadastrar_agencia(agencias)

    elif opcao == "4":
        listar_clientes(clientes)

    elif opcao == "5":
        listar_contas(contas)

    elif opcao == "6":
        listar_agencias(agencias)

    elif opcao == "7":
        sacar(contas)

    elif opcao == "8":
        transferir(contas)

    elif opcao == "9":
        depositar(contas)

    elif opcao == "10":
        consultar_saldo(contas)

    elif opcao == "11":
        relatorio_banco(clientes, contas, agencias)

    elif opcao == "12":
        salvar_dados(clientes, contas, agencias)

    elif opcao == "0":
        salvar_dados(clientes, contas, agencias)
        print("Programa encerrado.")

    else:
        print("Opção inválida.")