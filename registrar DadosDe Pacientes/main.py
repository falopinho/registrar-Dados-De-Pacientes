#Lógica por trás do código

nome = input("Nome: ")
idade = int(input("Idade: "))

cliente = nome,  idade
cliente2 = nome, idade

#Clientes
if idade < 65:
    with open("project/clientes/" + str(nome) + ".txt", "w") as arquivo:
            for valor in cliente:
                arquivo.write(str(valor) + "\n")
    print("Cliente adicionado com sucesso")

#Cliente grupo de risco
elif idade >= 65:
    with open("project/cliente grupo de risco/" + str(nome) + ".txt", "w") as arquivo:
        for valor in cliente2:
            arquivo.write(str(valor) + "\n")
    print("Cliente adicionado com sucesso")
else:
    print("OPÇÃO INVÁLIDA!")
