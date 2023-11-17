#Cadastro de clientes
def cadastro():

    #Nome
    def nome():


        nome = input("Nome Completo: ").lower()
            
        while True:
                 
            if all(c.isalpha() or c.isspace() for c in nome):
                return # sai do while
            else:
                nome = input("Por favor digite um nome válido (somente letras e espaços )\n").lower() 
    
    nome()

    #Email
    def email():

        email = str(input("Email: ")).lower()
        if len(email) <= 7:
                email = input("Seu email é muito curto.\npor favor escreva o email novamente: ").lower()
        while "@" and ".com" not in email:
            email = input("Seu email deve ter '@' e '.com'\npor favor escreva o email novamente: ").lower()


    email()

    #CPF
    def cpf():
         
        cpf = input("CPF: ")
        
        while True:
            if all(c.isnumeric() for c in cpf):
                return
            else:
                cpf = input("Só é permitido números no CPF.\npor favor escreva novamente: ")

            while True:
                if len(cpf) == 11:
                    return
                else:
                    cpf = input("Seu CPF precisa de 11 dígitos.\npor favor escreva novamente: ")

              
    cpf()

    #RG
    def rg():
        while True:
            rg = input("RG: ").lower()
            if len(rg) == 10:
                return
            else:
                rg = input("Seu RG precisa de 10 dígitos.\npor favor escreva novamente: ").lower()
        

    rg()

    #Telefone
    def tel():
        while True:

            tel = input("Telefone: ")
            if len(tel) == 11:
                return
            else:
                tel = input("Seu número de TELEFONE precisa de 11 dígitos,\npor favor escreva novamente: ")

    tel()

    #Nascimento
    def nascimento():
        nascimento = input("Data de Nascimento: ")
        ano = int(nascimento[4:8])

        idade = (2023 - ano) #Obtendo idade

        while True:
            if len(nascimento) == 8:
                return
            else:
                nascimento = input("Sua data de nascimento, precisa de 8 dígitos, e não pode conter '/'\npor favor escreva novamente: ")

            while True:
                if all(c.isnumeric() for c in nascimento):
                    return
                else:
                    nascimento = input("Só é permitido números no nascimentos\npor favor escreva novamente: ")

    nascimento()