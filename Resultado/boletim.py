from conexao import conectar

def boletim_da_urna():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato GROUP BY c.Id, c.Nome, c.Num_votacao, c.Partido ORDER BY c.Nome"
    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n== BOLETIM DE URNA ==")
    for nome, numero, partido, total in resultados:
        print(f"Candidato: {nome} | Número: {numero} | Partido: {partido} | Votos: {total}")


    sql_vencedor = "SELECT c.Nome, c.Num_votacao, c.Partido, COUNT(v.Id) as total FROM candidatos c LEFT JOIN votos v ON c.Id = v.Candidato GROUP BY c.Id ORDER BY total DESC LIMIT 1"
    cursor.execute(sql_vencedor)
    vencedor = cursor.fetchone()

    print("\n== VENCEDOR ==")
    print(f"Nome: {vencedor[0]} | Número: {vencedor[1]} | Partido: {vencedor[2]} | Votos: {vencedor[3]}")
    cursor.close() 
    conexao.close() 
    input("\nPressione Enter para continuar...")