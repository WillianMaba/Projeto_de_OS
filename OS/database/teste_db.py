from OS.database import *
from OS.database.conexao import criar_conexao
from OS.database.tabelasdb import criar_tabela


def verificar_tabelas():
    con = criar_conexao()
    cur = con.cursor()

    # Mostra todas as tabelas existentes no banco
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cur.fetchall()

    con.close()

    if tabelas:
        print("\n📋 Tabelas encontradas no banco de dados:")
        for tabela in tabelas:
            print(f" - {tabela[0]}")
    else:
        print("⚠️ Nenhuma tabela foi encontrada.")

# --------------------------------------------------------
# Execução do teste
# --------------------------------------------------------
if __name__ == "__main__":
    print("🔧 Criando tabelas...")
    criar_tabela()         # cria todas as tabelas
    print("\n🔍 Verificando banco de dados...")
    verificar_tabelas()    # lista o que foi criado
