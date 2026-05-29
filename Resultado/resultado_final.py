from conexao import conectar

def resultado_final():
    """
    Exibe o resultado final da eleição com o candidato vencedor.
    Oferece a opção de listar a votação completa de todos os candidatos.

    Args:
        Nenhum.

    Returns:
        None: Imprime o resultado no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql_vencedor = """
        SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total 
        FROM candidatos c 
        LEFT JOIN votos v ON c.Id = v.Candidato 
        GROUP BY c.Id 
        ORDER BY total DESC 
    """
    cursor.execute(sql_vencedor)
    resultados = cursor.fetchall() # Obtém todos os candidatos ordenados por votos

    max_votos= resultados[0][3]
    vecedores =[r for r in resultados if r[3] == max_votos]

    if len(vecedores) > 1:
        print("\n== RESULTADO FINAL ==")
        print("Houve um empate entre os seguintes candidatos:")
        for nome, numero, partido, total in vecedores:
            print(f"{nome} | Número: {numero} | Partido: {partido} | Votos: {total}")
        print("\nSerá necessário um segundo turno para determinar o vencedor.")
        cursor.close()
        conexao.close()
        return

    vencedor = resultados[0] # O candidato com mais votos é o vencedor
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