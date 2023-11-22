#Lógica por trás do código

nome = input("Nome: ")
idade = int(input("Idade: "))

cliente = nome,  idade
cliente2 = nome, idade

    
if idade < 65:
    with open(str(nome) + ".txt", "w") as arquivo:
            for valor in cliente:
                arquivo.write(str(valor) + "\n")

    print("Cliente adicionado com sucesso")

elif idade >= 65:
    with open(str(nome) + ".txt", "w") as arquivo:
        for valor in cliente2:
            arquivo.write(str(valor) + "\n")
else:
    print("OPÇÃO INVÁLIDA!")
