import tkinter as tk
from OS.GUI import cliente_gui, tecnico_gui, servico_gui, os_gui

root = tk.Tk(); root.title("Sistema de OS"); root.geometry("400x450")

tk.Label(root, text="Sistema de OS", font=("Arial",20)).pack(pady=20)
tk.Button(root, text="Cadastrar Cliente", width=30, command=cliente_gui.tela_cadastro_cliente).pack(pady=5)
tk.Button(root, text="Cadastrar Técnico", width=30, command=tecnico_gui.tela_cadastro_tecnico).pack(pady=5)
tk.Button(root, text="Nova Ordem de Serviço", width=30, command=os_gui.tela_nova_os).pack(pady=5)
tk.Button(root, text="Cadastrar Serviço", width=30, command=servico_gui.tela_cadastro_servico).pack(pady=5)
tk.Button(root, text="Consultar Clientes", width=30, command=cliente_gui.tela_consulta_cliente).pack(pady=5)
tk.Button(root, text="Consultar Técnicos", width=30, command=tecnico_gui.tela_consulta_tecnico).pack(pady=5)
tk.Button(root, text="Consultar Serviços", width=30, command=servico_gui.tela_consulta_servico).pack(pady=5)
tk.Button(root, text="Apagar Cliente", width=30, command=cliente_gui.apagar_cliente).pack(pady=5)
tk.Button(root, text="Apagar Técnico", width=30, command=tecnico_gui.apagar_tecnico).pack(pady=5)
tk.Button(root, text="Apagar Serviço", width=30, command=servico_gui.apagar_servico).pack(pady=5)
tk.Button(root, text="Sair", width=30, command=root.quit).pack(pady=20)

root.mainloop()
