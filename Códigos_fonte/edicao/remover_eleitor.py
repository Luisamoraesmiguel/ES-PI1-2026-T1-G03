from conexao import conectar

def apagar_eleitor_do_banco(titulo_digitado):
     """
    Remove permanentemente um eleitor do banco de dados
    com base no número do título eleitoral informado.

    Args:
        titulo_digitado (str): Número do título do eleitor a ser removido.

    Returns:
        None: Executa a remoção e exibe confirmação no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    comando_sql = "DELETE FROM eleitores WHERE titulo = %s"
    cursor.execute(comando_sql, (titulo_digitado,))

    conexao.commit()
    print(f"\n[SUCESSO] Eleitor com título {titulo_digitado} removido com sucesso!")

    cursor.close() 
    conexao.close()

def apagar_candidato_do_banco(numero_digitado):
    """
    Remove permanentemente um candidato do banco de dados
    com base no número do título eleitoral informado.

    Args:
        titulo_digitado (str): Número do título do eleitor a ser removido.

    Returns:
        None: Executa a remoção e exibe confirmação no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    comando_sql = "DELETE FROM candidatos WHERE num_votacao = %s"
    cursor.execute(comando_sql, (numero_digitado,))

    conexao.commit()
    print(f"\n[SUCESSO] Candidato com número {numero_digitado} removido com sucesso!")

    cursor.close() 
    conexao.close()

