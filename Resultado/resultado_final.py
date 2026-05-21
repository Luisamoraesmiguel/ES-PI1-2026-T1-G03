from conexao import conectar

def resultado_final():
    conexao = conectar()
    cursor = conexao.cursor()

    sql_vencedor = """
        SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total 
        FROM candidatos c 
        LEFT JOIN votos v ON c.Id = v.Candidato 
        GROUP BY c.Id 
        ORDER BY total DESC 
        LIMIT 1
    """
    cursor.execute(sql_vencedor)
    vencedor = cursor.fetchone()

    print("\n== RESULTADO FINAL ==")
    print(f"Vencedor: {vencedor[0]}")
    print(f"Número:   {vencedor[1]}")
    print(f"Partido:  {vencedor[2]}")
    print(f"Votos:    {vencedor[3]}")

    ver = input("\nDeseja ver a quantidade de votos de todos os candidatos? (S/N): ").upper().strip()

    if ver == "S":
        sql = """
            SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total 
            FROM candidatos c 
            LEFT JOIN votos v ON c.Id = v.Candidato 
            GROUP BY c.Id, c.Nome, c.Num_votacao, c.Partido 
            ORDER BY total DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\n== VOTOS POR CANDIDATO ==")
        for nome, numero, partido, total in resultados:
            print(f"{nome} | Número: {numero} | Partido: {partido} | Votos: {total}")

        print("\n pressione Enter para voltar...")
        input()
    cursor.close()
    conexao.close()