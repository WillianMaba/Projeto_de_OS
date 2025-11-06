from OS.Interface import linha
from OS.database import *
from OS.database.conexao import criar_conexao


#CRIAÇÃO DAS FUNÇÕES DE INSERIR NO BANCO DE DADOS

def inserir_clientes(nome, telefone, email, endereco):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''
            INSERT INTO clientes(nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
            ''',(nome, telefone, email, endereco))

        con.commit()
        print(f'Cliente {nome} criado com sucesso!')
    except Exception as e:
        print('❌ Erro ao inserir cliente!')
    finally:
        con.close()



def inserir_tecnico(nome, telefone, especialidade, email):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''
            INSERT INTO tecnicos(nome, telefone, especialidade, email)
            VALUES (?, ?, ?, ?)
            ''',(nome, telefone, especialidade, email))

        con.commit()
        print(f'Tecnico {nome} criado com sucesso!')
    except Exception as e:
        print('❌ Erro ao inserir técnico!')
    finally:
        con.close()



def inserir_ordens_servico(cliente_id, tecnico_id, descricao):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''
        INSERT INTO ordens_servico (cliente_id, tecnico_id, descricao)
        VALUES (?, ?, ?)
        ''',(cliente_id, tecnico_id, descricao))

        con.commit()
        print(f'Ordem de serviço criada com sucesso!')
    except Exception as e:
        print('❌ Erro ao inserir ordem de serviço!')
    finally:
        con.close()



def inserir_servico(nome, descricao, valor):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''
        INSERT INTO servicos(nome, descricao, valor)
        VALUES (?, ?, ?)
        ''',(nome, descricao, valor))

        con.commit()
        print('Serviço criado com sucesso!')
    except Exception as e:
        print('❌ Erro ao inserir serviço!')
    finally:
        con.close()



def inserir_itens_os(os_id, servico_id, quantidade, valor_unitario):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''
        INSERT INTO itens_os(os_id, servico_id, quantidade, valor_unitario)
        VALUES (?, ?, ?, ?)
        ''',(os_id, servico_id, quantidade, valor_unitario))

        con.commit()
        print('Item OS criado com sucesso!')
    except Exception as e:
        print('❌ Erro ao inserir serviço!')
    finally:
        con.close()


#CRIAÇÃO DAS FUNÇÕES DE VISUALIZAÇÃO


def ver_clientes():
    con = criar_conexao()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM clientes")
        clientes = cur.fetchall()
        return clientes
        print(ver_clientes())# retorna lista de tuplas
    except Exception as e:
        print("❌ Erro ao buscar clientes:", e)
        return []
    finally:
        con.close()



def ver_tecnicos():
    con = criar_conexao()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM tecnicos")
        tecnicos = cur.fetchall()
        return tecnicos
        print(ver_tecnicos())
    except Exception as e:
        print("❌ Erro ao buscar técnicos:", e)
        return []
    finally:
        con.close()



def ver_ordens_servico():
    con = criar_conexao()
    cur = con.cursor()
    try:
        cur.execute("""
            SELECT os.id, c.nome, t.nome, os.descricao, os.data
            FROM ordens_servico os
            JOIN clientes c ON os.cliente_id = c.id
            JOIN tecnicos t ON os.tecnico_id = t.id
        """)
        ordens = cur.fetchall()
        return ordens
        print(ver_ordens_servico())
    except Exception as e:
        print("❌ Erro ao buscar ordens de serviço:", e)
        return []
    finally:
        con.close()



def ver_servicos():
    con = criar_conexao()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM servicos")
        servicos = cur.fetchall()
        return servicos
        print(ver_servicos())
    except Exception as e:
        print("❌ Erro ao buscar serviços:", e)
        return []
    finally:
        con.close()



def ver_itens_os():
    con = criar_conexao()
    cur = con.cursor()
    try:
        cur.execute("""
            SELECT i.id, os.id, s.nome, i.quantidade, i.valor_unitario
            FROM itens_os i
            JOIN ordens_servico os ON i.os_id = os.id
            JOIN servicos s ON i.servico_id = s.id
        """)
        itens = cur.fetchall()
        return itens
        print(ver_itens_os())
    except Exception as e:
        print("❌ Erro ao buscar itens OS:", e)
        return []
    finally:
        con.close()


#CRIAÇÃO DAS FUNÇÕES DE ATUALIZAÇÃO

def atualizar_cliente(id_cliente, nome, telefone, email, endereco):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE clientes
                        SET nome = ?, telefone = ?, email = ?, endereco = ?
                    WHERE id = ?''',(nome, telefone, email, endereco, id_cliente))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Cliente ID {id_cliente} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum cliente encontrado com ID {id_cliente}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar cliente')
    finally:
        con.close()


def atualizar_tecnico(id_tecnico, nome, telefone, especialidade,email):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE tecnicos
                        SET nome = ?, telefone = ?, especialidade = ?,email = ?
                    WHERE id = ?''',(nome, telefone, especialidade, email,id_tecnico))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Técnico ID {id_tecnico} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum técnico encontrado com ID {id_tecnico}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar técnico')
    finally:
        con.close()


def atualizar_ordens_servico(id_os,cliente_id,tecnico_id,descricao,data_conclusao=None):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE ordens_servico
                        SET cliente_id = ?, tecnico_id = ?, descricao = ?,data_conclusao = ?
                    WHERE id = ?''',(cliente_id, tecnico_id, descricao, data_conclusao,id_os))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Ordem de serviço {id_os} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhuma Ordem de serviço encontrado com ID {id_os}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar Ordem de serviço')
    finally:
        con.close()


def atualizar_servico(id_servico, nome, descricao, valor):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE servicos
                        SET nome = ?, descricao = ?,valor = ?
                        WHERE id = ?''',(nome, descricao, valor,id_servico))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ serviço {id_servico} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum serviço encontrado com ID {id_servico}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar serviço')
    finally:
        con.close()


def atualizar_item_os(id_item, os_id, servico_id, quantidade, valor_unitario):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE itens_os
                        SET os_id = ?, servico_id = ?,quantidade = ?,valor_unitario = ?
                        WHERE id = ?''',(os_id, servico_id, quantidade, valor_unitario, id_item))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Item de OS {id_item} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum Item de OS encontrado com ID {id_item}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar Item de OS')
    finally:
        con.close()



#CRIAÇÃO DAS FUNÇÕES DE DELETAR


def deletar_cliente(id_cliente):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM clientes WHERE id = ?''', (id_cliente,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Cliente ID {id_cliente} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum cliente encontrado com ID {id_cliente}.')
    except Exception as e:
        print(f'❌ Erro ao excluir cliente:')
    finally:
        con.close()

def deletar_tecnico(id_tecnico):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM tecnicos WHERE id = ?''', (id_tecnico,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Técnico ID {id_tecnico} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum técnico encontrado com ID {id_tecnico}.')
    except Exception as e:
        print(f'❌ Erro ao excluir técnico:')
    finally:
        con.close()


def deletar_ordem_servico(id_ordem_servico):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM ordens_servico WHERE id = ?''', (id_ordem_servico,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Ordem de serviço ID {id_ordem_servico} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhuma ordem de serviço encontrado com ID {id_ordem_servico}.')
    except Exception as e:
        print(f'❌ Erro ao excluir ordem de serviço:')
    finally:
        con.close()


def deletar_servico(id_servico):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM servicos WHERE id = ?''', (id_servico,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Serviço ID {id_servico} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum serviço encontrado com ID {id_servico}.')
    except Exception as e:
        print(f'❌ Erro ao excluir serviço:')
    finally:
        con.close()

def deletar_item_os(id_item_os):
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM itens_os WHERE id = ?''', (id_item_os,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Itens OS ID {id_item_os} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum item de OS encontrado com ID {id_item_os}.')
    except Exception as e:
        print(f'❌ Erro ao excluir item de OS:')
    finally:
        con.close()