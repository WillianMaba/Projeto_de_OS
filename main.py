from OS.Interface import *
from time import sleep

print(linha())
print('\033[1;031m Sistema de OS \033[m'.center(50))
print(linha())


while True:
    print('1-Cadastrar Cliente\n'
          '2-Cadastrar Técnico\n'
          '3-Nova Ordem de Serviço\n'
          '4-Novo Serviço\n'
          '5-Novo Item OS\n'
          '6-Ver Clientes\n'
          '7-Ver Técnicos\n'
          '8-Ver Ordem de Serviço\n'
          '9-Ver Serviços\n'
          '10-Ver itens OS\n'
          '11-Apagar Clientes\n'
          '12-Apagar Serviço\n'
          '0_Sair ')

    try:
        opçoes = int(input('Escolha sua opção: '))
    except:
        print('Digite Apenas números inteiros!')
        continue

    if opçoes == 1:
        while True:
            print(linha())
            print('Cadastro de Cliente'.center(50))
            try:
                id_cliente = int(input('Digite o ID do Cliente: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                nome = str(input('Nome: '))
                Telefone = str(input('Telefone: '))
                email = str(input('Email: '))
                endereço = str(input('Endereço: '))
                sleep(1)
                print(linha())
                print('\033[0;32m Cliente Cadastrado com sucesso! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja cadastrar novo cliente? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break


    elif opçoes == 2:
        while True:
            print(linha())
            print('Cadastro de Técnicos'.center(50))
            try:
                id_tecnico = int(input('Digite o ID do Técnico: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                nome = str(input('Nome: '))
                Telefone = str(input('Telefone: '))
                especialidade = str(input('Especialidade: '))
                email = str(input('Email: '))
                sleep(1)
                print(linha())
                print('\033[0;32m Técnico Cadastrado com sucesso! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja cadastrar novo funcionário? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 3:
        while True:
            print(linha())
            print('Nova Ordem de Serviço'.center(50))
            try:
                id_os = int(input('Digite o ID da OS: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                descricao = str(input('Descricao: '))
                data_abertura = str(input('Data abertura: '))
                status = str(input('Status: '))
                valor_total = str(input('Valor Total: '))
                cliente = str(input('Cliente: '))
                tecnico = str(input('Tecnico: '))
                sleep(1)
                print(linha())
                print('\033[0;32m Nova ordem de serviço criada! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja cadastrar nova ordem de serviço? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 4:
        while True:
            print(linha())
            print('Novo Serviço'.center(50))
            try:
                id_serviço = int(input('Digite o ID do serviço: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                nome = str(input('Nome: '))
                preco_base = str(input('Preço Base: '))
                sleep(1)
                print(linha())
                print('\033[0;32m Novo serviço criado com sucesso! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja cadastrar novo serviço? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 5:
        while True:
            print(linha())
            print('Novo Item OS'.center(50))
            try:
                os_id = int(input('ID do Os: '))
                serviço_id = int(input('ID do serviço: '))
                quantidade = int(input('Quantidade: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                valor_unitario = str(input('Valor Unitario: '))
                sleep(1)
                print(linha())
                print('\033[0;32m Novo Item OS Criado com sucesso! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja cadastrar novo item OS? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 6 :
        while True:
            print(linha())
            print('Consulta geral'.center(50))
            print(linha())
            try:
                cliente = int(input('ID do cliente: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                print(cliente)
                resposta = pergunta_continuar('Deseja visualizar mais clientes? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 7:
        while True:
            print(linha())
            print('Consulta geral'.center(50))
            print(linha())
            try:
                tecnico = int(input('ID do técnico: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                print(tecnico)
                resposta = pergunta_continuar('Deseja visualizar mais técnicos? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 8:
        while True:
            print(linha())
            print('Consulta geral'.center(50))
            print(linha())
            try:
                ordem_servico = int(input('ID do OS: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                print(ordem_servico)
                resposta = pergunta_continuar('Deseja visualizar mais ordem de serviço? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 9:
        while True:
            print(linha())
            print('Consulta geral'.center(50))
            print(linha())
            try:
                servico = int(input('ID do Serviço: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                print(servico)
                resposta = pergunta_continuar('Deseja visualizar mais serviços? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 10:
        while True:
            print(linha())
            print('Consulta geral'.center(50))
            print(linha())
            try:
                iten_os = int(input('ID do item de OS: '))
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
            else:
                print(iten_os)
                resposta = pergunta_continuar('Deseja visualizar mais itens OS? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 11:
        while True:
            try:
                print(linha())
                apagar_cliente = int(input('Digite o ID do Cliente que deseja apagar: '))
                print(linha())
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
                print(linha())
            else:
                print(f'APAGANDO CLIENTE {apagar_cliente}...')
                sleep(1)
                print('\033[0;32m Cliente apagado com sucesso! \033[m ')
                print(linha())
                resposta = pergunta_continuar('Deseja apagar mais clientes? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break


    elif opçoes == 12:
        while True:
            try:
                print(linha())
                apagar_servico = str(input('Digite o ID do Serviço que deseja apagar: '))
                print(linha())
            except:
                print('\033[0;31m Digite Apenas números inteiros! \033[m')
                print(linha())
            else:
                print(f'APAGANDO SERVIÇO {apagar_servico}...')
                sleep(1)
                print('\033[0;32m Serviço apagado com sucesso! \033[m')
                print(linha())
                resposta = pergunta_continuar('Deseja apagar mais serviços? [S/N]: ')
                if resposta == 'n':
                    print('Muito Obrigado! Volte Sempre!')
                    break

    elif opçoes == 0:
        print(linha())
        print('\033[0;31m ENCERRANDO PROGRAMA \033[m')
        print('\033[0;31m Muito Obrigado!Volte Sempre! \033[m')
        print(linha())
        break
