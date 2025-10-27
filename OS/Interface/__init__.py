def linha(tam = 50):
    return '-' * 50

def pergunta_continuar(msg='Deseja continuar? [S/N]: '):
    while True:
        resposta = input(msg).strip().lower()

        # Normaliza palavras mais longas
        if resposta in ['s', 'sim']:
            return 's'
        elif resposta in ['n', 'nao', 'não']:
            return 'n'
        else:
            print('\033[0;31mDigite apenas S, N, Sim ou Não!\033[m')


