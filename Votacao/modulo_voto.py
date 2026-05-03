from conexao import conectar

def realizar_votacao():
    conexao = conectar()
    cursor = conexao.cursor()

    titulo=input("Digite o seu Título de Eleitor: ")
    voto=input("Digite o número do seu candidato: ")

    comando_sql = "INSERT INTO votos (titulo, numero, data_voto) VALUES (%s, %s, NOW())"
    dados_voto = (titulo, voto)
    cursor.execute(comando_sql, dados_voto)
    conexao.commit()
    print(f"Voto confirmado para o candidato {voto}!")
    cursor.close()
    conexao.close()
    
