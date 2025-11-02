import tkinter as tk
from tkinter import messagebox, ttk
from OS.database import operadores

def tela_cadastro_cliente():
    janela = tk.Toplevel()
    janela.title("Cadastro de Cliente")
    janela.geometry("350x300")

    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela); nome_entry.pack()
    tk.Label(janela, text="Telefone:").pack()
    telefone_entry = tk.Entry(janela); telefone_entry.pack()
    tk.Label(janela, text="Email:").pack()
    email_entry = tk.Entry(janela); email_entry.pack()
    tk.Label(janela, text="Endereço:").pack()
    endereco_entry = tk.Entry(janela); endereco_entry.pack()

    def salvar_cliente():
        nome = nome_entry.get(); telefone = telefone_entry.get()
        email = email_entry.get(); endereco = endereco_entry.get()
        if nome and telefone:
            operadores.inserir_clientes(nome, telefone, email, endereco)
            messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Nome e Telefone obrigatórios!")

    tk.Button(janela, text="Salvar", command=salvar_cliente).pack(pady=10)

def tela_consulta_cliente():
    janela = tk.Toplevel()
    janela.title("Consulta de Clientes")
    janela.geometry("600x400")
    tree = ttk.Treeview(janela, columns=("ID", "Nome", "Telefone", "Email", "Endereço"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    clientes = operadores.ver_clientes()
    for c in clientes: tree.insert("", "end", values=c)

def apagar_cliente():
    janela = tk.Toplevel()
    janela.title("Apagar Cliente")
    janela.geometry("300x150")

    tk.Label(janela, text="Digite o ID do Cliente para apagar:").pack(pady=5)
    id_entry = tk.Entry(janela)
    id_entry.pack(pady=5)

    def deletar():
        try:
            id_cliente = int(id_entry.get())
            operadores.deletar_cliente(id_cliente)
            messagebox.showinfo("Sucesso", f"Cliente ID {id_cliente} apagado!")
            janela.destroy()
        except ValueError:
            messagebox.showwarning("Erro", "Digite apenas números inteiros!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao apagar cliente: {e}")

    tk.Button(janela, text="Apagar", command=deletar).pack(pady=10)
