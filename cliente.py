def nome(nome):
    if nome.isalpha() and nome.isspace():
        return("Nome válido")
    else:
        return("Caracteres inválidos")

def docs(cpf, dataN):
    if cpf.isnumeric() and dataN.isnumeric():
        return("Documento válido")
    else:
        return("Caracteres inválidos")
print(nome(input('Digite seu nome: ')))
print(docs(input('Digite seu CPF: '), input('Digite sua data de nascimento: ')))