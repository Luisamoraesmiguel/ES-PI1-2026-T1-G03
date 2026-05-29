from conexao import conectar

def apagar_eleitor_do_banco(titulo_digitado):
        
    conexao = conectar()
    cursor = conexao.cursor()

    comando_sql = "DELETE FROM eleitores WHERE titulo = %s"
    cursor.execute(comando_sql, (titulo_digitado,))

    conexao.commit()
    print(f"\n[SUCESSO] Eleitor com título {titulo_digitado} removido com sucesso!")

    cursor.close() 
    conexao.close()

def apagar_candidato_do_banco(numero_digitado):
        
    conexao = conectar()
    cursor = conexao.cursor()

    comando_sql = "DELETE FROM candidatos WHERE num_votacao = %s"
    cursor.execute(comando_sql, (numero_digitado,))

    conexao.commit()
    print(f"\n[SUCESSO] Candidato com número {numero_digitado} removido com sucesso!")

    cursor.close() 
    conexao.close()

