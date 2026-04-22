import mysql.connector

def apagar_eleitor_do_banco(titulo_digitado):
    """
    Remove um eleitor da tabela usando o numero do titulo.
    """
    try:
        # 1. Abre a conexao (Use a sua senha aqui!)
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="tabela_bd"
        )
        cursor = conexao.cursor()

        # 2. Comando para DELETAR (Onde o titulo for igual ao digitado)
        comando_sql = "DELETE FROM eleitores WHERE titulo = %s"
        cursor.execute(comando_sql, (titulo_digitado,))

        # 3. Salva a mudanca
        conexao.commit()
        print("Sucesso: Comando de remocao enviado!")

    except Exception as e:
        print(f"Erro ao remover: {e}")

    finally:
        if conexao.is_connected():
            conexao.close()

