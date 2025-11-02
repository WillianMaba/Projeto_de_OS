import tkinter as tk
from tkinter import messagebox, ttk
from OS.database import operadores

def tela_nova_os():
    janela = tk.Toplevel(); janela.title("Nova Ordem de Serviço"); janela.geometry("400x300")

    tk.Label(janela, text="ID do Cliente:").pack(); cliente_entry = tk.Entry(janela); cliente_entry.pack()
    tk.Label(janela, text="ID do Técnico:").pack(); tecnico_entry = tk.Entry(janela); tecnico_entry.pack()
    tk.Label(janela, text="Descrição:").pack(); desc_entry = tk.Entry(janela); desc_entry.pack()
    tk.Label(janela, text="Data (YYYY-MM-DD):").pack(); data_entry = tk.Entry(janela); data_entry.pack()

    def salvar_os():
        try:
            cid = int(cliente_entry.get()); tid = int(tecnico_entry.get())
        except: messagebox.showwarning("Erro","IDs devem ser numéricos"); return
        desc = desc_entry.get(); data = data_entry.get()
        operadores.inserir_ordens_servico(cid, tid, desc, data)
        messagebox.showinfo("Sucesso","Ordem de Serviço cadastrada!"); janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar_os).pack(pady=10)


def novo_item_os():
    janela = tk.Toplevel()
    janela.title("Novo Item OS")
    janela.geometry("350x250")

    tk.Label(janela, text="ID da OS:").pack(); os_entry = tk.Entry(janela); os_entry.pack()
    tk.Label(janela, text="ID do Serviço:").pack(); serv_entry = tk.Entry(janela); serv_entry.pack()
    tk.Label(janela, text="Quantidade:").pack(); quant_entry = tk.Entry(janela); quant_entry.pack()
    tk.Label(janela, text="Valor Unitário:").pack(); valor_entry = tk.Entry(janela); valor_entry.pack()

    def salvar_item():
        try:
            os_id = int(os_entry.get())
            serv_id = int(serv_entry.get())
            quantidade = int(quant_entry.get())
            valor = float(valor_entry.get())
            operadores.inserir_itens_os(os_id, serv_id, quantidade, valor)
            tk.messagebox.showinfo("Sucesso", "Item OS cadastrado!")
            janela.destroy()
        except ValueError:
            tk.messagebox.showwarning("Erro", "Digite valores numéricos válidos")
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao cadastrar item OS: {e}")

    tk.Button(janela, text="Salvar", command=salvar_item).pack(pady=10)


def consultar_itens_os():
    janela = tk.Toplevel()
    janela.title("Itens de OS")
    janela.geometry("600x400")

    tree = ttk.Treeview(janela, columns=("ID Item","ID OS","Serviço","Quantidade","Valor Unitário"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True)

    itens = operadores.ver_itens_os()
    for i in itens:
        tree.insert("", "end", values=i)
