from conexao import conectar
from Criptografia import cifrar

def editar_candidato():
    """
    Permite editar os dados de um candidato cadastrado no banco.
    O operador pode alterar nome, número de votação ou partido.

    Args:
        Nenhum.

    Returns:
        None: Aplica as alterações no banco e exibe confirmação.
    """
    print("\n== EDIÇÃO DE CANDIDATO ==")
    numero = input("Digite o número do candidato que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM candidatos WHERE Num_votacao = %s", (numero,))
    candidato = cursor.fetchone()

    if candidato is None:
        print("[ERRO] Candidato não encontrado.")
        input("\nPressione Enter para voltar...") # Adicionado para dar tempo de ler
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
        if novo.strip() == "" or novo.isdigit():
            print("Nome inválido. Por favor, tente novamente.")
            input("\nPressione Enter para voltar...")
            cursor.close()
            conexao.close()
            return
        cursor.execute("UPDATE candidatos SET Nome = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Nome atualizado para {novo} com sucesso!")

    elif opcao == "2":
        novo = input("Novo número: ")
        if not novo.isdigit():
            print("Número inválido. Por favor, tente novamente.")
            input("\nPressione Enter para voltar...")
            cursor.close()
            conexao.close()
            return
        
        # --- NOVA TRAVA DE DUPLICIDADE AQUI ---
        # Verificamos se o NOVO número já pertence a OUTRO candidato antes de tentar o UPDATE
        cursor.execute("SELECT Nome FROM candidatos WHERE Num_votacao = %s", (novo,))
        conflito = cursor.fetchone()
        
        if conflito:
            print(f"\n[ERRO] O número {novo} já pertence ao candidato {conflito[0]}.")
            print("Operação abortada para evitar erro de duplicidade.")
            input("\nPressione ENTER para voltar...") # Pausa para você ler o erro
            cursor.close()
            conexao.close()
            return
        # --------------------------------------

        cursor.execute("UPDATE candidatos SET Num_votacao = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Número atualizado para {novo} com sucesso!")

    elif opcao == "3":
        novo = input("Novo partido: ")
        if novo.strip() == "":
            print("Partido inválido. Por favor, tente novamente.")
            input("\nPressione Enter para voltar...")
            cursor.close()
            conexao.close()
            return
        cursor.execute("UPDATE candidatos SET Partido = %s WHERE Num_votacao = %s", (novo, numero))
        print(f"Partido atualizado para {novo} com sucesso!")

    elif opcao == "0":
        cursor.close()
        conexao.close()
        return

    else:
        print("\nOpção inválida, Tente novamente.")
        input("\nPressione Enter para voltar...")
        cursor.close()
        conexao.close()
        return

    conexao.commit()
    print("\nCandidato atualizado com sucesso!")
    input("\nPressione Enter para concluir...") # Pausa final
    cursor.close()
    conexao.close()