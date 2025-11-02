import tkinter as tk
from tkinter import messagebox, ttk
from OS.database import operadores

def tela_cadastro_tecnico():
    janela = tk.Toplevel(); janela.title("Cadastro de Técnico"); janela.geometry("350x250")
    tk.Label(janela, text="Nome:").pack(); nome_entry = tk.Entry(janela); nome_entry.pack()
    tk.Label(janela, text="Telefone:").pack(); telefone_entry = tk.Entry(janela); telefone_entry.pack()
    tk.Label(janela, text="Especialidade:").pack(); esp_entry = tk.Entry(janela); esp_entry.pack()
    tk.Label(janela, text="Email:").pack(); email_entry = tk.Entry(janela); email_entry.pack()

    def salvar_tecnico():
        nome = nome_entry.get(); tel = telefone_entry.get(); esp = esp_entry.get(); email = email_entry.get()
        if nome and esp:
            operadores.inserir_tecnico(nome, tel, esp, email)
            messagebox.showinfo("Sucesso", f"Técnico {nome} cadastrado!"); janela.destroy()
        else:
            messagebox.showwarning("Erro", "Nome e Especialidade obrigatórios!")

    tk.Button(janela, text="Salvar", command=salvar_tecnico).pack(pady=10)

def tela_consulta_tecnico():
    janela = tk.Toplevel(); janela.title("Consulta de Técnicos"); janela.geometry("600x400")
    tree = ttk.Treeview(janela, columns=("ID","Nome","Telefone","Especialidade","Email"), show="headings")
    for col in tree["columns"]: tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)
    tecnicos = operadores.ver_tecnicos()
    for t in tecnicos: tree.insert("", "end", values=t)

def apagar_tecnico():
    janela = tk.Toplevel()
    janela.title("Apagar Técnico")
    janela.geometry("300x150")

    tk.Label(janela, text="Digite o ID do Técnico para apagar:").pack(pady=5)
    id_entry = tk.Entry(janela)
    id_entry.pack(pady=5)

    def deletar():
        try:
            id_tecnico = int(id_entry.get())
            operadores.deletar_tecnico(id_tecnico)
            messagebox.showinfo("Sucesso", f"Técnico ID {id_tecnico} apagado!")
            janela.destroy()
        except ValueError:
            messagebox.showwarning("Erro", "Digite apenas números inteiros!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao apagar técnico: {e}")

    tk.Button(janela, text="Apagar", command=deletar).pack(pady=10)
