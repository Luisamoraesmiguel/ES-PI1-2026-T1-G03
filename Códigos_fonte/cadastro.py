import mysql.connector

def cadastrar_eleitor(nome, titulo, cpf):
    """
    Funcao que envia os dados do eleitor para o banco de dados.

    Args:
        nome (str): Nome do eleitor.
        titulo (str): Numero do titulo.
        cpf (str): Numero do CPF.

    Returns:
        int: Retorna 1 se deu certo ou 0 se deu erro.
    """
    try:
        # Tenta conectar ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # Se tiver senha, coloque aqui
            database="tabela_bd"
        )
        
        cursor = conexao.cursor()

        # Comando para inserir os dados na tabela
        comando = "INSERT INTO eleitores (nome, titulo, cpf) VALUES (%s, %s, %s)"
        valores = (nome, titulo, cpf)

        cursor.execute(comando, valores)
        conexao.commit() 
        
        print("Cadastro realizado!")
        return 1

    except Exception as erro:
        print(f"Erro: {erro}")
        return 0

    finally:
        # Fecha a conexao para nao travar o banco
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()