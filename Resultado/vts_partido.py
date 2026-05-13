from conexao import conectar

def votos_por_partido():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato GROUP BY c.Partido ORDER BY total DESC"
    cursor.execute(sql)

    resultados = cursor.fetchall() # Cada linha é uma tupla (partido, total_votos)

    print("\n== VOTOS POR PARTIDO ==")
    for partido, total in resultados:
        print(f"Partido: {partido} | Votos: {total}")

    cursor.close()
    conexao .close()
    input("\nPressione Enter para continuar...")