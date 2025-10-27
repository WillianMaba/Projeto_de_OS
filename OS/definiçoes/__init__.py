from OS.Interface import *
from time import sleep


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
            consulta_servico()
        elif opcoes == 9:
            consulta_item_os()
        elif opcoes == 10:
            consulta_cliente()
        elif opcoes == 11:
            apagar_cliente()
        elif opcoes == 12:
            apagar_servico()
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
            id_cliente = int(input('Digite o ID do Cliente: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            endereco = input('Endereço: ')
            sleep(1)
            print(linha())
            sucesso('Cliente Cadastrado com sucesso!')
            print(linha())
            resposta = pergunta_continuar('Deseja cadastrar novo cliente? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def cadastrar_tecnico():
    while True:
        print(linha())
        print('Cadastro de Técnicos'.center(50))
        try:
            id_tecnico = int(input('Digite o ID do Técnico: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            especialidade = input('Especialidade: ')
            email = input('Email: ')
            sleep(1)
            print(linha())
            sucesso('Técnico Cadastrado com sucesso!')
            print(linha())
            resposta = pergunta_continuar('Deseja cadastrar novo funcionário? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def nova_ordem_servico():
    while True:
        print(linha())
        print('Nova Ordem de Serviço'.center(50))
        try:
            id_os = int(input('Digite o ID da OS: '))
            valor_total = float(input('Valor Total: '))
        except ValueError:
            erro('Digite apenas números válidos!')
        else:
            descricao = input('Descricao: ')
            data_abertura = input('Data abertura: ')
            status = input('Status: ')
            cliente = input('Cliente: ')
            tecnico = input('Tecnico: ')
            sleep(1)
            print(linha())
            sucesso('Nova ordem de serviço criada!')
            print(linha())
            resposta = pergunta_continuar('Deseja cadastrar nova ordem de serviço? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def novo_servico():
    while True:
        print(linha())
        print('Novo Serviço'.center(50))
        try:
            id_servico = int(input('Digite o ID do serviço: '))
            preco_base = float(input('Preço Base: '))
        except ValueError:
            erro('Digite apenas números válidos!')
        else:
            nome = input('Nome: ')
            sleep(1)
            print(linha())
            sucesso('Novo serviço criado com sucesso!')
            print(linha())
            resposta = pergunta_continuar('Deseja cadastrar novo serviço? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def novo_item_os():
    while True:
        print(linha())
        print('Novo Item OS'.center(50))
        try:
            os_id = int(input('ID do Os: '))
            servico_id = int(input('ID do serviço: '))
            quantidade = int(input('Quantidade: '))
            valor_unitario = float(input('Valor Unitario: '))
        except ValueError:
            erro('Digite apenas números válidos!')
        else:
            sleep(1)
            print(linha())
            sucesso('Novo Item OS Criado com sucesso!')
            print(linha())
            resposta = pergunta_continuar('Deseja cadastrar novo item OS? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def consulta_cliente():
    while True:
        print(linha())
        print('Consulta geral'.center(50))
        print(linha())
        try:
            cliente = int(input('ID do cliente: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            print(cliente)
            resposta = pergunta_continuar('Deseja visualizar mais clientes? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def consulta_tecnico():
    while True:
        print(linha())
        print('Consulta geral'.center(50))
        print(linha())
        try:
            tecnico = int(input('ID do técnico: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            print(tecnico)
            resposta = pergunta_continuar('Deseja visualizar mais técnicos? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def consulta_os():
    while True:
        print(linha())
        print('Consulta geral'.center(50))
        print(linha())
        try:
            ordem_servico = int(input('ID do OS: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            print(ordem_servico)
            resposta = pergunta_continuar('Deseja visualizar mais ordem de serviço? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def consulta_servico():
    while True:
        print(linha())
        print('Consulta geral'.center(50))
        print(linha())
        try:
            servico = int(input('ID do Serviço: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            print(servico)
            resposta = pergunta_continuar('Deseja visualizar mais serviços? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def consulta_item_os():
    while True:
        print(linha())
        print('Consulta geral'.center(50))
        print(linha())
        try:
            item_os = int(input('ID do item de OS: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
        else:
            print(item_os)
            resposta = pergunta_continuar('Deseja visualizar mais itens OS? [S/N]: ')
            if resposta == 'n':
                print('Muito Obrigado! Volte Sempre!')
                break


def apagar_cliente():
    while True:
        print(linha())
        try:
            id_cliente = int(input('Digite o ID do Cliente que deseja apagar: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
            continue
        sucesso(f'Cliente {id_cliente} apagado com sucesso!')
        print(linha())
        if pergunta_continuar('Deseja apagar outro cliente? [S/N]: ') == 'n':
            break

def apagar_servico():
    while True:
        print(linha())
        try:
            id_servico = int(input('Digite o ID do Serviço que deseja apagar: '))
        except ValueError:
            erro('Digite Apenas números inteiros!')
            continue
        sucesso(f'Serviço {id_servico} apagado com sucesso!')
        print(linha())
        if pergunta_continuar('Deseja apagar outro serviço? [S/N]: ') == 'n':
            break


