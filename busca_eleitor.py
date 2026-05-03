from conexao import conectar
import Criptografia

def buscar_eleitor(dado):
    """
    Busca um eleitor utilizando a conexão própria e Cifra de Hill.
    
    Args:
        dado (str): CPF ou Título digitado pelo usuário.
    Returns:
        dict: Dados do eleitor ou None se não encontrado.
    """
    termo = dado.strip()

    conexao = conectar() 
    cursor = conexao.cursor(dictionary=True)

    if len(termo) == 11:
        termo_pesquisa = Criptografia.cifrar(termo)
        campo_sql = "cpf"
    else:
        termo_pesquisa = termo
        campo_sql = "titulo"

    query = f"SELECT nome, cpf, titulo, mesario FROM eleitores WHERE {campo_sql} = %s"

    cursor.execute(query, (termo_pesquisa,))
    resultado = cursor.fetchone()

    if resultado:
        print("\n" + "="*30)
        print("   ELEITOR ENCONTRADO")
        print("="*30)
        print(f"NOME:    {resultado['nome']}")
        print(f"TÍTULO:  {resultado['titulo']}")
        print(f"CPF:     {Criptografia.decifrar(resultado['cpf'])}")
        print(f"MESÁRIO: {'SIM' if resultado['mesario'] else 'NÃO'}")
        print("="*30 + "\n")
    else:
        print("\n" + "="*30)
        print("   ELEITOR NÃO ENCONTRADO")
        print("="*30 + "\n")

    cursor.close()
    conexao.close()

    return resultado
