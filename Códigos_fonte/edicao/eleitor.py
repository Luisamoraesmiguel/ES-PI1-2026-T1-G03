from conexao import conectar
from Criptografia import cifrar
from Códigos_fonte.validacoes.cpf import validar_cpf
from Códigos_fonte.validacoes.titulo import verificar_titulo

def editar_eleitor():
    print("\n== EDIÇÃO DE ELEITOR ==")
    titulo = input("Digite o título do eleitor que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM eleitores WHERE titulo = %s", (titulo,)) 
    eleitor = cursor.fetchone()

    if eleitor is None:
        print("\nEleitor não encontrado.")
        cursor.close()
        conexao.close()
        return

    print(f"\nEleitor encontrado: {eleitor[1]}")
    print("O que deseja editar?")
    print("1- Nome")
    print("2- Título")
    print("3- CPF")
    print("4- Mesário (S/N)")
    print("5- Chave de acesso")
    print("0- Voltar")

    opcao = input("Escolha: ")

    if opcao == "1":
        novo = input("Novo nome: ").upper().strip()
        cursor.execute("UPDATE eleitores SET nome = %s WHERE titulo = %s", (novo, titulo))
        conexao.commit() # salvar alteracoes no banco de dados
        print(f"Nome atualizado para {novo} com sucesso!")

    elif opcao == "2":
        novo = False
        while not novo:
            novo = input("Digite o número do título de eleitor: ")
            if verificar_titulo(novo):
                cursor.execute("SELECT titulo FROM eleitores WHERE titulo = %s", (novo,))
                if cursor.fetchone() is not None:
                    print("\nTítulo de eleitor já cadastrado. Tente novamente.")
                    novo = False
                else:
                    print("Título de eleitor válido.")
                    print(f"Título atualizado para {novo} com sucesso!")
                    cursor.execute("UPDATE eleitores SET titulo = %s WHERE titulo = %s", (novo, titulo))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
            else:
                print("Título de eleitor inválido. Por favor, tente novamente.")
                novo = False

        

    elif opcao == "3":
        novo = input("Novo CPF: ")
        if not validar_cpf(novo):
            print("CPF inválido. Por favor, tente novamente.")
            cursor.close()
            conexao.close()
            return
        novo_cifrado = cifrar(novo)
        cursor.execute("SELECT cpf FROM eleitores WHERE cpf = %s", (novo_cifrado,))
        if cursor.fetchone() is not None:
            print("\nCPF já cadastrado. Tente novamente.")
            cursor.close()
            conexao.close()
            return
        cursor.execute("UPDATE eleitores SET cpf = %s WHERE titulo = %s", (novo_cifrado, titulo))
        conexao.commit()
        print("CPF atualizado com sucesso!")

    elif opcao == "4":
        novo = input("É mesário? (S/N): ").upper()
        cursor.execute("UPDATE eleitores SET mesario = %s WHERE titulo = %s", (novo, titulo))
        conexao.commit()
        print(f"Status de mesário atualizado para {novo} com sucesso!")

    elif opcao == "5":
        novo = input("Nova chave de acesso: ").upper()
        novo_cifrado = cifrar(novo)
        cursor.execute("UPDATE eleitores SET chave_de_acesso = %s WHERE titulo = %s", (novo, titulo))
        conexao.commit()
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

    #conexao.commit() 
    #print("\nDados atualizados com sucesso!")
    #cursor.close()
    #conexao.close()

