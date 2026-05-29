from conexao import conectar
import os

def limpar_tela():
    """
    Limpa o terminal de acordo com o sistema operacional em uso.

    Args:
        Nenhum.

    Returns:
        None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def votos_por_candidato():
    """
    Consulta e exibe a contagem de votos agrupada por candidato,
    ordenando do mais votado para o menos votado.

    Args:
        Nenhum.

    Returns:
        None: Imprime o ranking de votos por candidato no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total 
        FROM candidatos c 
        LEFT JOIN votos v ON c.Id = v.Candidato 
        GROUP BY c.Id, c.Nome, c.Num_votacao, c.Partido 
        ORDER BY total DESC
    """
    cursor.execute(sql)
    resultados = cursor.fetchall() 

    limpar_tela()
    print(f"\n==== VOTOS POR CANDIDATO ====")

    if not resultados:
        print("Nenhum candidato cadastrado.")
    else:
        
         for nome, numero, partido, total in resultados:
            print(f"{numero} | {nome} ({partido}) - Votos: {total}")


    cursor.close()
    conexao.close()
    input("\nPressione Enter para voltar...")