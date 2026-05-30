from conexao import conectar

def boletim_da_urna():
    """
    Exibe o boletim de urna com a contagem de votos por candidato
    e destaca o vencedor da eleição.

    Args:
        Nenhum.

    Returns:
        None: Imprime o boletim e o vencedor no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato GROUP BY c.Id, c.Nome, c.Num_votacao, c.Partido ORDER BY c.Nome"
    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n== BOLETIM DE URNA ==")
    for nome, numero, partido, total in resultados:
        if numero == 0 or partido == 'NULO':
            votos_nulos = total
        else:

            print(f"Candidato: {nome} | Número: {numero} | Partido: {partido} | Votos: {total}")

    print("-" * 30)
    print(f"Votos Nulos e Brancos: {votos_nulos}")


    sql_vencedor = "SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato WHERE c.Num_votacao != 0 GROUP BY c.Id ORDER BY total DESC LIMIT 1"
    cursor.execute(sql_vencedor)
    vencedor = cursor.fetchone()

    if vencedor:
        print("\n== VENCEDOR PARCIAL ==")
        print(f"Nome: {vencedor[0]} | Número: {vencedor[1]} | Partido: {vencedor[2]} | Votos: {vencedor[3]}")
    else:
        print("\n== VENCEDOR PARCIAL ==\nNenhum candidato real recebeu votos válidos ainda.")

    cursor.close() 
    conexao.close() 
    input("\nPressione Enter para continuar...")