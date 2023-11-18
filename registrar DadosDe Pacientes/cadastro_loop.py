import cadastro

#Loop para continuar cadastrando clientes
def loop():                                            
    app = input("Deseja cadastrar um cliente? ").lower()

    while True:

        if app in ["sim", "s", "si"]:
            cadastro.nome()
            cadastro.email()
            cadastro.cpf()
            cadastro.rg()
            cadastro.tel()
            cadastro.nascimento()
            app = input("\nDeseja cadastrar um cliente? ").lower()
        elif app in ["não", "nao", "n", "na"]:
            break
        else:
            print("Essa não é uma opção válida, por favor tente novamente...\n")
            app = input("Deseja cadastrar um cliente? ").lower()
