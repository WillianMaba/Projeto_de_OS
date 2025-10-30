import sqlite3

#CRIAÇÃO DO BANCO DE DADOS E CONEXÃO
def criar_conexao():
    conexao = sqlite3.connect('database.db')
    return conexao
