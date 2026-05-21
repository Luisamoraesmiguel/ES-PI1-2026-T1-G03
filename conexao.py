import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Mede@2000', 
        database='tabela_bd'
    )
