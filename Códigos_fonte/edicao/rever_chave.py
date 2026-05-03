from conexao import conectar
def rever_chave_acesso():
    titulo = input("Digite o título do eleitor: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT chave_de_acesso FROM eleitores WHERE titulo = %s", (titulo,))
    resultado = cursor.fetchone() 
    if resultado:
        chave_de_acesso = resultado[0]
        print(f"A chave de acesso do eleitor com título {titulo} é: {chave_de_acesso}")
    
    else:
        print("Eleitor não encontrado.")
    cursor.close()
    conexao.close()

