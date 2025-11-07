from OS.Interface import *
from time import sleep
from OS.database import operadores, tabelasdb, conexao
from OS.database.operadores import *


def menu():
    while True:
        print(linha())
        print('\033[1;031m Sistema de OS \033[m'.center(50))
        print(linha())
        print('1-Cadastrar Cliente\n'
              '2-Cadastrar Técnico\n'
              '3-Nova Ordem de Serviço\n'
              '4-Novo Serviço\n'
              '5-Novo Item OS\n'
              '6-Ver Clientes\n'
              '7-Ver Técnicos\n'
              '8-Ver Ordem de Serviço\n'
              '9-Ver Serviços\n'
              '10-Ver Itens OS\n'
              '11-Apagar Clientes\n'
              '12-Apagar Serviço\n'
              '13-Apagar Técnico\n'
              '0-Sair ')

        try:
            opcoes = int(input('Escolha sua opção: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
            continue

        if opcoes == 1:
            cadastrar_cliente()
        elif opcoes == 2:
            cadastrar_tecnico()
        elif opcoes == 3:
            nova_ordem_servico()
        elif opcoes == 4:
            novo_servico()
        elif opcoes == 5:
            novo_item_os()
        elif opcoes == 6:
            consulta_cliente()
        elif opcoes == 7:
            consulta_tecnico()
        elif opcoes == 8:
            consulta_os()
        elif opcoes == 9:
            consulta_servico()
        elif opcoes == 10:
            consulta_item_os()
        elif opcoes == 11:
            apagar_cliente()
        elif opcoes == 12:
            apagar_servico()
        elif opcoes == 13:
            apagar_tecnico()
        elif opcoes == 0:
            print(linha())
            erro('ENCERRANDO PROGRAMA...')
            erro('Muito Obrigado! Volte Sempre!')
            print(linha())
            break
        else:
            erro('Opção inválida!')


def pergunta_continuar(msg='Deseja continuar? [S/N]: '):
    while True:
        resposta = input(msg).strip().lower()
        if resposta in ['s', 'sim']:
            return 's'
        elif resposta in ['n', 'nao', 'não']:
            return 'n'
        else:
            print('\033[0;31mDigite apenas S, N, Sim ou Não!\033[m')


def cadastrar_cliente():
    while True:
        print(linha())
        print('Cadastro de Cliente'.center(50))
        try:
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            endereco = input('Endereço: ')
            operadores.inserir_clientes(nome, telefone, email, endereco)
            sucesso(f'Cliente {nome} cadastrado com sucesso!')
            sleep(1)
        except Exception as e:
            print('Erro ao cadastrar cliente!')
        if pergunta_continuar('Deseja cadastrar novo cliente? [S/N]: ') == 'n':
            break


def cadastrar_tecnico():
    while True:
        print(linha())
        print('Cadastro de Técnicos'.center(50))
        try:
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            especialidade = input('Especialidade: ')
            email = input('Email: ')
            operadores.inserir_tecnico(nome, telefone, especialidade, email)
        except Exception as e:
            erro(f'Erro ao cadastrar técnico: {e}')

        if pergunta_continuar('Deseja cadastrar novo técnico? [S/N]: ') == 'n':
            break

def nova_ordem_servico():
    while True:
        print(linha())
        print('Nova Ordem de Serviço'.center(50))
        try:
            cliente_id = int(input('ID do Cliente: '))
            tecnico_id = int(input('ID do Técnico: '))
            descricao = input('Descrição: ')
            operadores.inserir_ordens_servico(cliente_id, tecnico_id, descricao)
        except ValueError:
            erro('Digite apenas números válidos!')
        except Exception as e:
            erro(f'Erro ao criar ordem de serviço: {e}')

        if pergunta_continuar('Deseja criar nova OS? [S/N]: ') == 'n':
            break


def novo_servico():
    while True:
        print(linha())
        print('Novo Serviço'.center(50))
        try:
            nome = input('Nome: ')
            descricao = input('Descrição: ')
            valor = float(input('Valor: '))
            operadores.inserir_servico(nome, descricao, valor)
        except ValueError:
            erro('Digite um valor numérico válido!')
        except Exception as e:
            erro(f'Erro ao cadastrar serviço: {e}')

        if pergunta_continuar('Deseja cadastrar novo serviço? [S/N]: ') == 'n':
            break


def novo_item_os():
    while True:
        print(linha())
        print('Novo Item OS'.center(50))
        try:
            os_id = int(input('ID da OS: '))
            servico_id = int(input('ID do Serviço: '))
            quantidade = int(input('Quantidade: '))
            valor_unitario = float(input('Valor Unitário: '))
            operadores.inserir_itens_os(os_id, servico_id, quantidade, valor_unitario)
        except ValueError:
            erro('Digite apenas números válidos!')
        except Exception as e:
            erro(f'Erro ao criar item OS: {e}')

        if pergunta_continuar('Deseja cadastrar novo item OS? [S/N]: ') == 'n':
            break


def consulta_cliente():
    operadores.ver_clientes()
    print(ver_clientes())
    input('Pressione ENTER para voltar ao menu...')

def consulta_tecnico():
    operadores.ver_tecnicos()
    print(ver_tecnicos())
    input('Pressione ENTER para voltar ao menu...')

def consulta_os():
    operadores.ver_ordens_servico()
    print(ver_ordens_servico())
    input('Pressione ENTER para voltar ao menu...')

def consulta_servico():
    operadores.ver_servicos()
    print(ver_servicos())
    input('Pressione ENTER para voltar ao menu...')

def consulta_item_os():
    operadores.ver_itens_os()
    print(ver_itens_os())
    input('Pressione ENTER para voltar ao menu...')


def apagar_cliente():
    while True:
        try:
            id_cliente = int(input('Digite o ID do Cliente que deseja apagar: '))
            operadores.deletar_cliente(id_cliente)
        except ValueError:
            erro('Digite apenas números inteiros!')
        except Exception as e:
            erro(f'Erro ao excluir cliente: {e}')

        if pergunta_continuar('Deseja apagar outro cliente? [S/N]: ') == 'n':
            break


def apagar_servico():
    while True:
        try:
            id_servico = int(input('Digite o ID do Serviço que deseja apagar: '))
            operadores.deletar_servico(id_servico)
        except ValueError:
            erro('Digite apenas números inteiros!')
        except Exception as e:
            erro(f'Erro ao excluir serviço: {e}')

        if pergunta_continuar('Deseja apagar outro serviço? [S/N]: ') == 'n':
            break


def apagar_tecnico():
    while True:
        try:
            id_tecnico = int(input('Digite o ID do Técnico que deseja apagar: '))
            operadores.deletar_tecnico(id_tecnico)
        except ValueError:
            erro('Digite apenas números inteiros!')
        except Exception as e:
            erro(f'Erro ao excluir técnico: {e}')

        if pergunta_continuar('Deseja apagar outro técnico? [S/N]: ') == 'n':
            break

