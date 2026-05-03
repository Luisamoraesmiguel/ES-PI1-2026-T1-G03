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
            print(f"Nome: {e[0]} | Título: {e[1]} | Mesário: {e[2]}")
    
    input("\nPressione Enter para voltar...")
   
