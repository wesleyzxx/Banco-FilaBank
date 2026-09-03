def nome(nome):
    if nome.isalpha() or nome.isspace:
        return("Nome válido")
    else:
        "Caracteres inválidos"

def docs(cpf, dataN):
    if cpf.isnumeric() and dataN.isnumeric():
        return("Documento válido")
    else:
        "Caracteres inválidos"
print(nome(input('Qual é o seu nome: ')))
print(docs(input('Qual é o seu cpf?: '), input('Em qual dia você nasceu?: ')))