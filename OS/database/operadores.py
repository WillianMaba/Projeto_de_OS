from OS.database import *
from OS.database.conexao import criar_conexao


#CRIAÇÃO DAS FUNÇÕES DE INSERIR NO BANCO DE DADOS

def inserir_clientes(nome, telefone, email, endereco):
    con = criar_conexao()
    cur = con.cursor()

    cur.execute('''
        INSERT INTO clientes(nome, telefone, email, endereco)
        VALUES (?, ?, ?, ?)
        ''',(nome, telefone, email, endereco))

    con.commit()
    con.close()
    print(f'Cliente {nome} criado com sucesso!')


def inserir_tecnico(nome, telefone, especialidade, email):
    con = criar_conexao()
    cur = con.cursor()

    cur.execute('''
        INSERT INTO tecnicos(nome, telefone, especialidade, email)
        VALUES (?, ?, ?, ?)
        ''',(nome, telefone, especialidade, email))

    con.commit()
    con.close()
    print(f'Tecnico {nome} criado com sucesso!')


def inserir_ordens_servico(cliente_id, tecnico_id, descricao):
    con = criar_conexao()
    cur = con.cursor()

    cur.execute('''
    INSERT INTO ordens_servico (cliente_id, tecnico_id, descricao)
    VALUES (?, ?, ?)
    ''',(cliente_id, tecnico_id, descricao))

    con.commit()
    con.close()
    print(f'Ordem de serviço criada com sucesso!')


def inserir_servico(nome, descricao, valor):
    con = criar_conexao()
    cur = con.cursor()

    cur.execute('''
    INSERT INTO servicos(nome, descricao, valor)
    VALUES (?, ?, ?)
    ''',(nome, descricao, valor))

    con.commit()
    con.close()
    print('Serviço criado com sucesso!')


def inserir_itens_os(os_id, servico_id, quantidade, valor_unitario):
    con = criar_conexao()
    cur = con.cursor()

    cur.execute('''
    INSERT INTO itens_os(os_id, servico_id, quantidade, valor_unitario)
    VALUES (?, ?, ?, ?)
    ''',(os_id, servico_id, quantidade, valor_unitario))

    con.commit()
    con.close()
    print('Item inserido com sucesso!')


#CRIAÇÃO DAS FUNÇÕES DE VISUALIZAÇÃO