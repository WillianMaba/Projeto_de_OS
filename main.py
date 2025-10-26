from OS.Interface import *
from time import sleep

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
      '10-Ver itens OS\n'
      '11-Apagar Clientes\n'
      '12-Apagar Serviço\n'
      '0_Sair ')


opçoes = int(input('Escolha sua opção: '))


while opçoes != 0:
        if opçoes == 1:
            print(linha())
            print('Cadastro de Cliente'.center(50))
            try:
             id_cliente = int(input('Digite o ID do Cliente: '))
            except:
                print('Digite Apenas números inteiros!')
            else:
                nome = str(input('Nome: '))
                Telefone = str(input('Telefone: '))
                email = str(input('Email: '))
                endereço = str(input('Endereço: '))
                sleep(1)
                print(linha())
                print('Cliente Cadastrado com sucesso!')
                print(linha())
                resposta = str(input('Deseja Cadastrar mais cliente? [S/N]: '))
                if resposta in 'nN':
                    print('Muito Obrigado!Volte Sempre!')
                    break


        if  opçoes == 2:
            print(linha())
            print('Cadastro de Técnicos'.center(50))
            try:
                id_tecnico = int(input('Digite o ID do Técnico: '))
            except:
                print('Digite Apenas números inteiros!')
            else:
                nome = str(input('Nome: '))
                Telefone = str(input('Telefone: '))
                especialidade = str(input('Especialidade: '))
                email = str(input('Email: '))
                sleep(1)
                print(linha())
                print('Técnico Cadastrado com sucesso!')
                print(linha())
                resposta = str(input('Deseja Cadastrar mais Técnicos? [S/N]: '))
                if resposta in 'nN':
                    print('Muito Obrigado!Volte Sempre!')
                    break

        if opçoes == 3:
            print(linha())
            print('Nova Ordem de Serviço'.center(50))
            id_os = int(input('Digite o ID da OS: '))
            descricao = str(input('Descricao: '))
            data_abertura = str(input('Data abertura: '))
            status = str(input('Status: '))
            valor_total = str(input('Valor Total: '))
            cliente = str(input('Cliente: '))
            tecnico = str(input('Tecnico: '))
            print(linha())

        if opçoes == 4:
            print(linha())
            print('Novo Serviço'.center(50))
            id_serviço = int(input('Digite o ID do serviço: '))
            nome = str(input('Nome: '))
            preco_base = str(input('Preço Base: '))
            print(linha())

        if opçoes == 5:
            print(linha())
            print('Novo Item OS'.center(50))
            os_id = int(input('ID do Os: '))
            serviço_id = int(input('ID do serviço: '))
            quantidade = str(input('Quantidade: '))
            valor_unitario = str(input('Valor Unitario: '))

        if opçoes == 6 == 7 == 8 == 9 == 10:
            print(linha())
            print('Consulta geral'.center(50))
            print()

        if opçoes == 11:
            print(linha())
            apagar_cliente = str(input('Digite o ID do Cliente que deseja apagar: '))
            print(linha())

        if opçoes == 12:
            print(linha())
            apagar_servico = str(input('Digite o ID do Serviço que deseja apagar: '))
            print('Serviço Excluido com Sucesso')
            print(linha())

        if opçoes == 0:
            print('Muito Obrigado!Volte Sempre!')
            break
