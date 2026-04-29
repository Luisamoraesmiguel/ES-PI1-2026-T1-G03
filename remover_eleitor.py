from conexao import conectar
import mysql.connector

def apagar_eleitor_do_banco(titulo_digitado):
        
    #try:    
        # 1. Abre a conexao (Use a sua senha aqui!)
    conexao = conectar()
    cursor = conexao.cursor()

        # 2. Comando para DELETAR (Onde o titulo for igual ao digitado)
        comando_sql = "DELETE FROM eleitores WHERE titulo = %s"
        cursor.execute(comando_sql, (titulo_digitado,))

        # 3. Salva a mudanca
        conexao.commit()
        print(f"\n[SUCESSO] Eleitor com título {titulo_digitado} removido com sucesso!")

    #except Exception as e:
        #print(f"Erro ao remover: {e}")

    #finally:
        #if conexao.is_connected():
        cursor.close() # Fecha o cursor
        conexao.close()

