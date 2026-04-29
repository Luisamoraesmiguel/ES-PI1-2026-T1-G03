from conexao import conectar
from Criptografia import cifrar

def editar_candidato():
    print("\n== EDIÇÃO DE CANDIDATO ==")
    numero = input("Digite o número do candidato que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM candidatos WHERE Num_votacao = %s", (numero,))
    candidato = cursor.fetchone()

    if candidato is None:
        print("[ERRO] Candidato não encontrado.")
        cursor.close()
        conexao.close()
        return

    print(f"\nCandidato encontrado: {candidato[1]}")
    print("O que deseja editar?")
    print("1- Nome")
    print("2- Número")
    print("3- Partido")
    print("0- Voltar")

    opcao = input("Escolha: ")

    if opcao == "1":
        novo = input("Novo nome: ")
        cursor.execute("UPDATE candidatos SET Nome = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Nome atualizado para {novo} com sucesso!")

    elif opcao == "2":
        novo = input("Novo número: ")
        cursor.execute("UPDATE candidatos SET Num_votacao = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Número atualizado para {novo} com sucesso!")

    elif opcao == "3":
        novo = input("Novo partido: ")
        cursor.execute("UPDATE candidatos SET Partido = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Partido atualizado para {novo} com sucesso!")

    elif opcao == "0":
        cursor.close()
        conexao.close()
        return

    else:
        print("Opção inválida, Tente novamente.")
        cursor.close()
        conexao.close()
        return

    conexao.commit()
    print("\nCandidato atualizado com sucesso!")
    cursor.close()
    conexao.close()