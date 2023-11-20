import customtkinter as ctk
import buttom

menu = ctk.CTk()
menu.title("Cadastro de Pacientes")
menu.geometry('500x300')


#Configurando janela menu
texto = ctk.CTkLabel(menu, text="Cadastro de Pacientes")
texto.pack(padx="10", pady="20")

texto1 = ctk.CTkLabel(menu, text="Deseja cadastrar um cliente?")
texto1.pack(padx="10", pady="10")

#configurando janela main
def main ():
    main = ctk.CTkToplevel(menu)
    main.geometry('500x300')
    main.title("Cadastro de Pacientes")
    

#botões sim e não
botao = ctk.CTkButton(master=menu, text="Sim", command=main)
botao.pack(padx="10", pady="20")

botao1 = ctk.CTkButton(menu, text="Não", command=buttom.desligar)
botao1.pack(padx="10", pady="20")


menu.mainloop()
