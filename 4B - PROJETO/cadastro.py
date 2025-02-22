import tkinter as tk
from tkinter import messagebox
import os

# Função de login
def verificar_login():
    usuario_digitado = entrada_usuario.get()
    senha_digitada = entrada_senha.get()

    if usuario_digitado == "MariaLuiza" and senha_digitada == "22222":
        login_janela.destroy()
        abrir_cadastro()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def abrir_cadastro():
    def salvar_cadastro():
        nome = entrada_nome.get()
        numero = entrada_numero.get()
        email = entrada_email.get()
        endereco = entrada_endereco.get()
        cargo = entrada_cargo.get()
        turno = entrada_turno.get()

        if not nome or not numero or not email or not endereco or not cargo or not turno:
            label_status.config(text="Todos os campos são obrigatórios!", fg="red")
            return

        if not numero.isdigit():
            label_status.config(text="Número inválido!", fg='red')
            return
        
        if '@gmail.com' not in email:
            label_status.config(text='Email inválido! O email precisa ser @gmail.com', fg='red')
            return
        
        with open("cadastros.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome}, Número: {numero}, Email: {email}, Endereço: {endereco}, Cargo: {cargo}, Turno: {turno}\n")

        label_status.config(text="Cadastro salvo com sucesso!", fg="green")
        limpar_campos()

    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_numero.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_endereco.delete(0, tk.END)
        entrada_cargo.delete(0, tk.END)
        entrada_turno.delete(0, tk.END)

    def sair_programa():
        janela.destroy()

    def mostrar_cadastros():
        nova_janela = tk.Toplevel(janela)
        nova_janela.geometry("700x400")
        nova_janela.title("Lista de Cadastros")
        nova_janela.configure(bg="darkslategray")

        largura_tela = nova_janela.winfo_screenwidth()
        altura_tela = nova_janela.winfo_screenheight()
        largura_janela = 1000
        altura_janela = 500
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        nova_janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        frame_cadastros = tk.Frame(nova_janela, bg="darkslategray")
        frame_cadastros.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        colunas = ["Nome", "Número", "Email", "Endereço", "Cargo", "Turno"]
        for i, coluna in enumerate(colunas):
            label = tk.Label(frame_cadastros, text=coluna, font=("Helvetica", 12, "bold"), relief="solid", width=15, anchor="w", bg="midnightblue", fg="white")
            label.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

        if os.path.exists("cadastros.txt"):
            with open("cadastros.txt", "r") as arquivo:
                cadastros = arquivo.readlines()

                for i, cadastro in enumerate(cadastros):
                    dados = cadastro.strip().split(", ")
                    for j, dado in enumerate(dados):
                        label = tk.Label(frame_cadastros, text=dado.split(": ")[1], font=("Helvetica", 10), relief="solid", width=15, anchor="w", bg="gray")
                        label.grid(row=i+1, column=j, padx=5, pady=5, sticky="ew")
        else:
            label = tk.Label(frame_cadastros, text="Nenhum cadastro encontrado.", font=("Helvetica", 10), width=90)
            label.grid(row=1, column=0, columnspan=6, pady=10)

        botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy, bg="tomato", fg="white", relief="raised", font=("Helvetica", 10))
        botao_fechar.pack(pady=10)

    janela = tk.Tk()
    janela.geometry('400x350')
    janela.title("Cadastro de Usuários")
    janela.configure(bg="darkslategray")

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    largura_janela = 400
    altura_janela = 350
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    frame_central = tk.Frame(janela, bg="darkslategray")
    frame_central.place(relx=0.5, rely=0.5, anchor="center")

    titulo = tk.Label(frame_central, text="Cadastre um funcionário", font=("Helvetica", 16, "bold"), bg="midnightblue", fg="white", pady=10)
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame_central, text="Nome:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=1, column=0, pady=5, padx=5, sticky="e")
    entrada_nome = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_nome.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(frame_central, text="Número:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=2, column=0, pady=5, padx=5, sticky="e")
    entrada_numero = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_numero.grid(row=2, column=1, pady=5, padx=5)

    tk.Label(frame_central, text="Email:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=3, column=0, pady=5, padx=5, sticky="e")
    entrada_email = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_email.grid(row=3, column=1, pady=5, padx=5)

    tk.Label(frame_central, text="Endereço:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=4, column=0, pady=5, padx=5, sticky="e")
    entrada_endereco = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_endereco.grid(row=4, column=1, pady=5, padx=5)

    tk.Label(frame_central, text="Cargo:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=5, column=0, pady=5, padx=5, sticky="e")
    entrada_cargo = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_cargo.grid(row=5, column=1, pady=5, padx=5)

    tk.Label(frame_central, text="Turno de Trabalho:", bg="darkslategray", font=("Helvetica", 10), fg="white").grid(row=6, column=0, pady=5, padx=5, sticky="e")
    entrada_turno = tk.Entry(frame_central, width=30, font=("Helvetica", 10))
    entrada_turno.grid(row=6, column=1, pady=5, padx=5)

    frame_botoes = tk.Frame(frame_central, bg="darkslategray")
    frame_botoes.grid(row=7, column=0, columnspan=2, pady=10)

    botao_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_cadastro, bg="forestgreen", fg="white", relief="raised", font=("Helvetica", 10))
    botao_salvar.pack(side="left", padx=10)

    botao_sair = tk.Button(frame_botoes, text="Sair", command=sair_programa, bg="tomato", fg="white", relief="raised", font=("Helvetica", 10))
    botao_sair.pack(side="left", padx=10)

    botao_mostrar = tk.Button(frame_botoes, text="Ver Cadastros", command=mostrar_cadastros, bg="royalblue", fg="white", relief="raised", font=("Helvetica", 10))
    botao_mostrar.pack(side="left", padx=10)

    label_status = tk.Label(frame_central, text="", fg="green", bg="darkslategray", font=("Helvetica", 10))
    label_status.grid(row=8, column=0, columnspan=2, pady=10)

    janela.mainloop()

login_janela = tk.Tk()
login_janela.title("Tela de Login")
login_janela.geometry("300x200")
login_janela.configure(bg="midnightblue")

# Centraliza a janela de login
largura_tela = login_janela.winfo_screenwidth()
altura_tela = login_janela.winfo_screenheight()
largura_janela = 300
altura_janela = 200
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
login_janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

label_usuario = tk.Label(login_janela, text="Usuário:", bg="midnightblue", fg="white")
label_usuario.pack(pady=5)

entrada_usuario = tk.Entry(login_janela)
entrada_usuario.pack(pady=5)

label_senha = tk.Label(login_janela, text="Senha:", bg="midnightblue", fg="white")
label_senha.pack(pady=5)

entrada_senha = tk.Entry(login_janela, show="*")
entrada_senha.pack(pady=5)

botao_login = tk.Button(login_janela, text="Entrar", command=verificar_login, bg="forestgreen", fg="white")
botao_login.pack(pady=20)

login_janela.mainloop()