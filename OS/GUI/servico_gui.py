import tkinter as tk
from tkinter import messagebox, ttk
from OS.database import operadores

def tela_cadastro_servico():
    janela = tk.Toplevel(); janela.title("Cadastro de Serviço"); janela.geometry("350x250")
    tk.Label(janela, text="Nome:").pack(); nome_entry = tk.Entry(janela); nome_entry.pack()
    tk.Label(janela, text="Descrição:").pack(); desc_entry = tk.Entry(janela); desc_entry.pack()
    tk.Label(janela, text="Valor:").pack(); valor_entry = tk.Entry(janela); valor_entry.pack()

    def salvar_servico():
        nome = nome_entry.get(); desc = desc_entry.get()
        try: valor = float(valor_entry.get())
        except: messagebox.showwarning("Erro","Valor inválido"); return
        if nome:
            operadores.inserir_servico(nome, desc, valor)
            messagebox.showinfo("Sucesso", f"Serviço {nome} cadastrado!"); janela.destroy()
        else:
            messagebox.showwarning("Erro","Nome obrigatório!")

    tk.Button(janela, text="Salvar", command=salvar_servico).pack(pady=10)

def tela_consulta_servico():
    janela = tk.Toplevel(); janela.title("Consulta de Serviços"); janela.geometry("600x400")
    tree = ttk.Treeview(janela, columns=("ID","Nome","Descrição","Valor"), show="headings")
    for col in tree["columns"]: tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)
    servicos = operadores.ver_servicos()
    for s in servicos: tree.insert("", "end", values=s)

def apagar_servico():
    janela = tk.Toplevel()
    janela.title("Apagar Serviço")
    janela.geometry("300x150")

    tk.Label(janela, text="Digite o ID do Serviço para apagar:").pack(pady=5)
    id_entry = tk.Entry(janela)
    id_entry.pack(pady=5)

    def deletar():
        try:
            id_servico = int(id_entry.get())
            operadores.deletar_servico(id_servico)
            messagebox.showinfo("Sucesso", f"Serviço ID {id_servico} apagado!")
            janela.destroy()
        except ValueError:
            messagebox.showwarning("Erro", "Digite apenas números inteiros!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao apagar serviço: {e}")

    tk.Button(janela, text="Apagar", command=deletar).pack(pady=10)
