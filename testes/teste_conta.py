import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cadastrarcontas import procurar_conta

contas = [
    {
        "numero": 1,
        "cpf": "52998224725",
        "agencia": 1,
        "tipo": "corrente",
        "saldo": 500
    }
]

conta = procurar_conta(contas, 1)

if conta != {}:
    print("Teste 1: busca de conta - OK")
else:
    print("Teste 1: busca de conta - ERRO")

conta = procurar_conta(contas, 2)

if conta == {}:
    print("Teste 2: conta inexistente - OK")
else:
    print("Teste 2: conta inexistente - ERRO")