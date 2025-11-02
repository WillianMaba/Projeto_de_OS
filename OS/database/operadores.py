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

        if not clientes:
            print('⚠️ Nenhum cliente encontrado!')
        else:
            print(linha())
            print("LISTA DE CLIENTES")
            print(linha())
            for cliente in clientes:
                print(f"ID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Telefone: {cliente[2]}")
                print(f"Email: {cliente[3]}")
                print(f"Endereco: {cliente[4]}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar cliente", e)
    finally:
        con.close()


def ver_tecnicos():
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute("SELECT * FROM tecnicos")
        tecnicos = cur.fetchall()

        if not tecnicos:
            print('⚠️ Nenhum tecnico encontrado!')
        else:
            print(linha())
            print("LISTA DE TÉCNICOS")
            print(linha())
            for tecnico in tecnicos:
                print(f"ID: {tecnico[0]}")
                print(f"Nome: {tecnico[1]}")
                print(f"Telefone: {tecnico[2]}")
                print(f"Especialidade: {tecnico[3]}")
                print(f"Email: {tecnico[4]}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar técnico", e)
    finally:
        con.close()


def ver_ordens_servico():
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''SELECT os.id,c.nome AS cliente,t.nome AS tecnico,os.descricao,os.data_abertura,os.data_conclusao
                       FROM ordens_servico AS os
                       LEFT JOIN clientes AS c ON os.cliente_id = c.id
                       LEFT JOIN tecnicos AS t ON os.tecnico_id = t.id
                       ORDER BY os.id
                    ''')
        ordens = cur.fetchall()

        if not ordens:
            print("⚠️ Nenhuma ordem de serviço encontrada.")
        else:
            print(linha())
            print("LISTA DE ORDENS DE SERVIÇO")
            print(linha())
            for ordem in ordens:
                print(linha())
                print(f"ID OS: {ordem[0]}")
                print(f"Cliente: {ordem[1]}")
                print(f"Técnico: {ordem[2]}")
                print(f"Descrição: {ordem[3]}")
                print(f"Data de Abertura: {ordem[4]}")
                print(f"Data de Conclusão: {ordem[5] if ordem[5] else 'Em aberto'}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar ordens de serviço:", e)
    finally:
        con.close()


def ver_servicos():
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute("SELECT * FROM servicos")
        servicos = cur.fetchall()

        if not servicos:
            print('⚠️ Nenhum serviço encontrado!')
        else:
            print(linha())
            print("LISTA DE SERVIÇOS")
            print(linha())
            for servico in servicos:
                print(f"ID: {servico[0]}")
                print(f"Nome: {servico[1]}")
                print(f"Descricao: {servico[2]}")
                print(f"Valor: {servico[3]:.2f}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar serviço!")
    finally:
        con.close()


def ver_itens_os():
    con = criar_conexao()
    cur = con.cursor()

    try:
        cur.execute('''SELECT ios.id,ios.os_id,s.descricao AS servico,ios.quantidade,ios.valor_unitario,(ios.quantidade * ios.valor_unitario) AS total_item
                       FROM itens_os AS ios
                       LEFT JOIN servicos AS s ON ios.servico_id = s.id
                       ORDER BY ios.os_id
                    ''')

        itens = cur.fetchall()

        if not itens:
            print("⚠️ Nenhum item de ordem de serviço encontrado.")
        else:
            print(linha())
            print("ITENS DE ORDEM DE SERVIÇO")
            print(linha())
            for item in itens:
                print(f"ID Item: {item[0]}")
                print(f"OS ID: {item[1]}")
                print(f"Serviço: {item[2]}")
                print(f"Quantidade: {item[3]}")
                print(f"Valor Unitário: R$ {item[4]:.2f}" if item[4] else "Valor Unitário: -")
                print(linha())

    except Exception as e:
        print("❌ Erro ao buscar itens da OS:", e)
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
        cur.execute('''UPDATE servicos
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
        cur.execute('''UPDATE itens
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
        cur.execute('''DELETE FROM ordem_servico WHERE id = ?''', (id_ordem_servico,))
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
        cur.execute('''DELETE FROM iten_os WHERE id = ?''', (id_item_os,))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Itens OS ID {id_item_os} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum item de OS encontrado com ID {id_item_os}.')
    except Exception as e:
        print(f'❌ Erro ao excluir item de OS:')
    finally:
        con.close()