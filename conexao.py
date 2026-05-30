import mysql.connector

def conectar():
    """
    Cria e retorna uma conexão com o banco de dados MySQL do sistema.

    Args:
        Nenhum.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão
        ativo com o banco de dados tabela_bd.
    """
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='sabrina9728', 
        database='tabela_bd'
    )
