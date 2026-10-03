import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cliente import validar_cpf

print("=== TESTE DE CPF ===")

cpf = "52998224725"

if validar_cpf(cpf):
    print("Teste 1: CPF válido - OK")
else:
    print("Teste 1: CPF válido - ERRO")

cpf = "12345678900"

if validar_cpf(cpf):
    print("Teste 2: CPF inválido - ERRO")
else:
    print("Teste 2: CPF inválido - OK")