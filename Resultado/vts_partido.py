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

    votos_nulos = 0

    for partido, total in resultados:
        if partido == 'NULO':
            votos_nulos = total
        else:
            print(f"Partido: {partido} | Votos: {total}")

    print("-" * 30)
    print(f"VOTOS NULOS (Sem Partido): {votos_nulos}")

    cursor.close()
    conexao .close()
    input("\nPressione Enter para continuar...")
