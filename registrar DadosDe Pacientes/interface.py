import customtkinter
import buttom

janela = customtkinter.CTk()
janela.title("Cadastro de Pacientes")
janela.geometry('500x300')

texto = customtkinter.CTkLabel(janela, text="Cadastro de Pacientes")
texto.pack(padx="10", pady="20")

texto1 = customtkinter.CTkLabel(janela, text="Deseja cadastrar um cliente?")
texto1.pack(padx="10", pady="10")

botao = customtkinter.CTkButton(janela, text="Sim" )
botao.pack(padx="10", pady="20")

botao1 = customtkinter.CTkButton(janela, text="Não", command=buttom.desligar)
botao1.pack(padx="10", pady="20")

janela.mainloop()
