from conexao import conectar

def votos_por_partido():
    """
    Consulta e exibe a contagem de votos agrupada por partido,
    ordenando do partido mais votado para o menos votado.

    Args:
        Nenhum.

    Returns:
        None: Imprime o total de votos por partido no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato GROUP BY c.Partido ORDER BY total DESC"
    cursor.execute(sql)

    resultados = cursor.fetchall() 

    print("\n== VOTOS POR PARTIDO ==")
    for partido, total in resultados:
        print(f"\nPartido: {partido} | Votos: {total}")

    cursor.close()
    conexao .close()
    input("\nPressione Enter para continuar...")
