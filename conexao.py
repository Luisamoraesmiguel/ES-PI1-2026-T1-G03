import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Beatriz_190524',
        database='tabela_bd'
    )
#conectar()
#from conexao import conectar
