import cadastro

#Loop para continuar cadastrando clientes
def cadastro_loop():                                            
    app = input("Deseja cadastrar um cliente? ").lower()

    while True:

        if app in ["sim", "s", "si"]:
            cadastro.cadastro()
        elif app in ["não", "nao", "n", "na"]:
            break
        else:
            print("Essa não é uma opção válida, por favor tente novamente...\n")
            cadastro_loop()

cadastro_loop()