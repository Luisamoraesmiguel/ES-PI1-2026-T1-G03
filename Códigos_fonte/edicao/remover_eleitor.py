from conexao import conectar
import mysql.connector

def apagar_eleitor_do_banco(titulo_digitado):
        
    conexao = conectar()
    cursor = conexao.cursor()

    comando_sql = "DELETE FROM eleitores WHERE titulo = %s"
    cursor.execute(comando_sql, (titulo_digitado,))

    conexao.commit()
    print(f"\n[SUCESSO] Eleitor com título {titulo_digitado} removido com sucesso!")

    cursor.close() 
    conexao.close()

