import mysql.connector

# Essa é a função que o professor quer
def gravar_voto_no_banco(numero_escolhido):
    """
    Guarda o voto do candidato no banco de dados.
    """
    try:
        # 1. Conecta no MySQL (Porta de entrada)
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tabela_bd"
        )
        cursor = conexao.cursor()

        # 2. Comando para INSERIR o dado
        comando_sql = "INSERT INTO votos (numero_candidato) VALUES (%s)"
        cursor.execute(comando_sql, (numero_escolhido,))

        # 3. Salva a mudança (Obrigatório)
        conexao.commit()
        print("Sucesso: Voto registrado!")

    except:
        # Se der erro (ex: banco desligado), avisa aqui
        print("Erro: Nao foi possivel salvar o voto.")

    finally:
        # 4. Fecha a conexão sempre
        conexao.close()

