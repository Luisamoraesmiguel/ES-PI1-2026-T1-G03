from conexao import conectar

def listar_eleitores():
    from conexao import conectar
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, titulo, mesario FROM eleitores")
    eleitores = cursor.fetchall()
    cursor.close()
    conexao.close()

    if not eleitores:
        print("Nenhum eleitor cadastrado.")
    else:
        print("\n== LISTA DE ELEITORES ==")
        for e in eleitores:
            print(f"\nNome: {e[0]} | Título: {e[1]} | Mesário: {e[2]}")
    
    input("\nPressione Enter para voltar...")
   
def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, partido, num_votacao FROM candidatos")
    candidatos = cursor.fetchall()
    cursor.close()
    conexao.close()

    if not candidatos:
        print("Nenhum candidato cadastrado.")
    else:
        print("\n== LISTA DE CANDIDATOS ==")
        for c in candidatos:
            print(f"Nome: {c[0]} | Partido: {c[1]} | Número: {c[2]}")
    
    input("\nPressione Enter para voltar...")
