def cadastro():
    #Nome
    nome = input("Digite um nome: ").lower()
    if all(a.isalpha() or a.isspace() for a in nome):
        pass
    else:
        nome = input("Essa não é uma opção válida, por favor tente novamente: ").lower()
    

    #Email
    email = input("Digite o email: ")
    if len(email) <= 7:
        email = input("O email é muito curto, por favor digite o email novamente: ").lower()
    while "@" and ".com" not in email:
        email = input("Seu email deve ter '@' e '.com'\npor favor escreva o email novamente: ").lower()


    #CPF
    cpf = str(input("Digite o CPF: "))
    if all(b.isnumeric() or b.isspace() for b in cpf):
        pass
    elif len(cpf) != 11:
        cpf = input("Seu CPF precisa de 11 dígitos.\npor favor escreva novamente: ")
    
    else:
        cpf = input("Só é permitido números no CPF.\npor favor escreva novamente: ")


    #RG 
    rg = str(input("Digite o RG: ")).lower()
    if len(rg) == 10:
        pass
    else:
        rg = input("Seu RG precisa de 10 dígitos.\npor favor escreva novamente: ").lower()


    #TEL
    tel = str(input("Digite o Telefone: "))
    if all(c.isnumeric() and c.isspace() for c in tel):
        pass
    elif len(tel) != 11:
        tel = input("Seu telefone precisa de 11 dígitos.\npor favor escreva novamente: ")
    else:
        tel = input("Seu número de TELEFONE precisa de 11 dígitos e não é permitido letras,\npor favor escreva novamente: ")

    
    #Idade
    idade = int(input("Digite o Idade: "))


    #importa dados para a pasta
    cliente = nome, email, cpf, rg, tel, idade
    cliente2 = nome, email, cpf, rg, tel, idade

    if idade < 65:
        with open("./pacientes/" + str(nome) + ".txt", "w") as arquivo:
            for valor in cliente:
                arquivo.write(str(valor) + "\n")
        print("Paciente adicionado em 'pacientes' com sucesso.")

    elif idade >= 65:
        with open("./paciente grupo de risco/" + str(nome) + ".txt", "w") as arquivo2:
            for valor2 in cliente2:
                arquivo2.write(str(valor2) + "\n")
        print("Paciente adicionado em 'paciente grupo de risco' com sucesso.")
