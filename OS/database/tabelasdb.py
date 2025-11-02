from OS.database import *
from OS.database.conexao import criar_conexao

#CRIAÇÃO DAS TABELAS PARA O BANCO DE DADOS
def criar_tabela():
    con = criar_conexao()
    cur = con.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            endereco TEXT
            )
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tecnicos (
            id INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT,
            especialidade TEXT,
            email TEXT
            )
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS ordens_servico (
             id INTEGER NOT NULL PRIMARY KEY,
             cliente_id INTEGER NOT NULL,
             tecnico_id INTEGER NOT NULL,
             descricao TEXT NOT NULL,
             data_abertura TEXT DEFAULT CURRENT_TIMESTAMP,
             data_conclusao TEXT,
             FOREIGN KEY(cliente_id) REFERENCES clientes(id),
             FOREIGN KEY(tecnico_id) REFERENCES tecnicos(id)
             )
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS servicos (
             id INTEGER NOT NULL PRIMARY KEY,
             nome TEXT NOT NULL,
             descricao TEXT,
             valor REAL NOT NULL
             )
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS itens_os (
             id INTEGER NOT NULL PRIMARY KEY,
             os_id INTEGER NOT NULL,
             servico_id INTEGER NOT NULL,
             quantidade INTEGER DEFAULT 1,
             valor_unitario REAL,
             FOREIGN KEY (os_id) REFERENCES ordens_servico (id),
             FOREIGN KEY (servico_id) REFERENCES servicos (id)
             )
    ''')

    con.commit()
    con.close()