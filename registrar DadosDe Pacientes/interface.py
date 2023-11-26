import customtkinter as ctk
import buttom

menu = ctk.CTk()
menu.title("Cadastro de Pacientes")
menu.geometry('800x500')
menu.resizable(width="False", height="False")


#Configurando janela menu
texto = ctk.CTkLabel(menu, text="Cadastro de Pacientes")
texto.pack(padx="10", pady="40")

texto1 = ctk.CTkLabel(menu, text="Deseja cadastrar um cliente?")
texto1.pack(padx="10", pady="50")

#Nova Janela
def main():
    main = ctk.CTkToplevel(menu, fg_color="white")
    main.geometry('800x500')
    main.resizable(width="False", height="False")
    main.mainloop()

#botões sim e não
botao = ctk.CTkButton(master=menu, text="Sim", command=main)
botao.pack(padx="10", pady="30")

botao1 = ctk.CTkButton(menu, text="Não", command=buttom.desligar)
botao1.pack(padx="10", pady="30")


menu.mainloop()
