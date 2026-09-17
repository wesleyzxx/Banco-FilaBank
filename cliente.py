print("=== CADASTRO DE CLIENTE ===")
nome = input("Nome completo: ")
cpf = input("CPF: ")
data_nascimento = input("Data de nascimento: ")

def cadastrar_cliente():
    print("=== DADOS DO CLIENTE ===")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Data de nascimento:", data_nascimento)
    return(nome)