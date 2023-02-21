import customtkinter
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()

janela.geometry("500x300")

def clique():
    print("login")

texto= customtkinter.CTkLabel( janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email= customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
email.pack(padx=10, pady=10)

senha= customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox=customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)



botao = customtkinter.CTkButton(janela, text= "login", command= clique)
botao.pack(padx=10, pady=10)






janela.mainloop() 
