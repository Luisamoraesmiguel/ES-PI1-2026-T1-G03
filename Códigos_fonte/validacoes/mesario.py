def verificar_mesario(titulo, cpf, chave):
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='tabela_bd'
    )   
    cursor = conexao.cursor()
    
    # Comando SQL para verificar se o mesário existe no banco de dados
    sql = f'''SELECT mesario FROM eleitores
                WHERE titulo = '{titulo}' 
                AND LEFT(cpf, 4) = '{cpf}' 
                AND chave_de_acesso = '{chave}' '''
    
    cursor.execute(sql)
    resultado = cursor.fetchone() # Pega o resultado da consulta
    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados
    if resultado and resultado[0] == 'S': # Verifica se o mesário existe e é um mesário
        return True
    else:
        return False