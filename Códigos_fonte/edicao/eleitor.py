from conexao import conectar
from Criptografia import cifrar

def editar_eleitor():
    print("\n== EDIÇÃO DE ELEITOR ==")
    titulo = input("Digite o título do eleitor que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM eleitores WHERE titulo = %s", (titulo,)) 
    eleitor = cursor.fetchone()

    if eleitor is None:
        print(" Eleitor não encontrado.")
        cursor.close()
        conexao.close()
        return

    print(f"\nEleitor encontrado: {eleitor[2]}")
    print("O que deseja editar?")
    print("1- Nome")
    print("2- Título")
    print("3- CPF")
    print("4- Mesário (S/N)")
    print("5- Chave de acesso")
    print("0- Voltar")

    opcao = input("Escolha: ")

    if opcao == "1":
        novo = input("Novo nome: ")
        cursor.execute("UPDATE eleitores SET nome = %s WHERE titulo = %s", (novo, titulo))
        print(f"Nome atualizado para {novo} com sucesso!")

    elif opcao == "2":
        novo = input("Novo título: ")
        cursor.execute("UPDATE eleitores SET titulo = %s WHERE titulo = %s", (novo, titulo))
        print(f"Título atualizado para {novo} com sucesso!")    

    elif opcao == "3":
        novo = input("Novo CPF: ")
        novo_cifrado = cifrar(novo)
        cursor.execute("UPDATE eleitores SET cpf = %s WHERE titulo = %s", (novo_cifrado, titulo))
        print("CPF atualizado para {novo} com sucesso!")

    elif opcao == "4":
        novo = input("É mesário? (S/N): ").upper()
        cursor.execute("UPDATE eleitores SET mesario = %s WHERE titulo = %s", (novo, titulo))
        print(f"Status de mesário atualizado para {novo} com sucesso!")

    elif opcao == "5":
        novo = input("Nova chave de acesso: ").upper()
        cursor.execute("UPDATE eleitores SET chave_de_acesso = %s WHERE titulo = %s", (novo, titulo))
        print(f"Chave de acesso ({novo}) atualizada com sucesso!")

    elif opcao == "0":
        cursor.close()
        conexao.close()
        return

    else:
        print("Opção inválida, Tente novamente.")
        cursor.close()
        conexao.close()
        return

    conexao.commit() # Salva as alterações no banco de dados
    print("\nDados atualizados com sucesso!")
    cursor.close()
    conexao.close()

