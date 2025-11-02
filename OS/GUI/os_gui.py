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
