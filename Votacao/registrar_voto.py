from conexao import conectar
from datetime import datetime

def gravar_voto_no_banco(numero_escolhido, titulo_eleitor, data_hora_voto):

    conexao = conectar()
    cursor = conexao.cursor()

    data_hora_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Formata a data e hora para o formato do MySQL
    
    comando_sql = "INSERT INTO votos (numero_candidato, data_hora_voto) VALUES (%s, %s)"
    cursor.execute(comando_sql, (numero_escolhido, data_hora_voto)) # Registra o voto na tabela de votos

    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) # Atualiza o status do eleitor para "votou = 'S'"
    
    conexao.commit()
    print("Sucesso: Voto registrado!")
    print(f"Protocolo: {data_hora_voto} - Candidato: {numero_escolhido}")

    cursor.close()
    conexao.close()

