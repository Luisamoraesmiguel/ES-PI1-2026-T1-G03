from conexao import conectar
from datetime import datetime

# Essa é a função que o professor quer
def gravar_voto_no_banco(numero_escolhido):
    #try:
        # 1. Abre a conexao 

    conexao = conectar()
    cursor = conexao.cursor()


    # Pegar data e hora do voto
    data_hora_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Formata a data e hora para o formato do MySQL
    
    #Registrar voto na tabela de votos
    comando_sql = "INSERT INTO votos (numero_candidato, data_hora_voto) VALUES (%s, %s)"
    cursor.execute(comando_sql, (numero_escolhido, data_hora_voto)) # Registra o voto na tabela de votos

    # Atualizar os status do eleitor
    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) # Atualiza o status do eleitor para "votou = 'S'"
    
    # Salvar as mudanças no banco de dados
    conexao.commit()
    print("Sucesso: Voto registrado!")
    print(f"Protocolo: {data_hora_voto} - Candidato: {numero_escolhido}")

    #except:
        # Se der erro (ex: banco desligado), avisa aqui
        #print("Erro: Nao foi possivel salvar o voto.")

    #finally:
        # 4. Fecha a conexão sempre
    cursor.close()
    conexao.close()

