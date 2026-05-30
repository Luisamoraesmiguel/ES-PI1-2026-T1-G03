from conexao import conectar
import Criptografia

def buscar_eleitor(dado):
    """
    Busca um eleitor no banco pelo CPF ou pelo título eleitoral.
    O CPF é cifrado antes da consulta pois é armazenado criptografado.

    Args:
        dado (str): CPF (11 dígitos) ou número do título eleitoral.

    Returns:
        dict: Dicionário com nome, cpf, titulo e mesario do eleitor,
              ou None se não encontrado.
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
        print(f"\nNOME:    {resultado['nome']}")
        print(f"TÍTULO:  {resultado['titulo']}")
        print(f"CPF:     {Criptografia.decifrar_cpf(resultado['cpf'])}")
        print(f"MESÁRIO: {'SIM' if resultado['mesario'] else 'NÃO'}")
        print("="*30 + "\n")
        input("Pressione Enter para retornar")
    else:
        print("\n" + "="*30)
        print("\n   ELEITOR NÃO ENCONTRADO")
        print("="*30 + "\n")
        input("Pressione Enter para retornar")

    cursor.close()
    conexao.close()

     

def buscar_candidato(numero):
    """
    Busca um candidato no banco de dados pelo número de votação.

    Args:
        numero (str ou int): Número de votação do candidato.

    Returns:
        dict: Dicionário com id, nome, numero e partido do candidato,
              ou None se não encontrado.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = "SELECT * FROM candidatos WHERE Num_votacao = %s"
    cursor.execute(sql, (numero,))
    resultado = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    if resultado is None:
        print("\n" + "="*30)
        print("\n  CANDIDATO NÃO ENCONTRADO")
        print("="*30 + "\n")
        input("Pressione Enter para retornar")
        return None

    print("\n" + "="*30)
    print("  CANDIDATO ENCONTRADO")
    print("="*30)
    print(f"\nNOME:    {resultado[1]}")
    print(f"NÚMERO:  {resultado[2]}")
    print(f"PARTIDO: {resultado[3]}")
    print("="*30 + "\n")
    input("Pressione Enter para retornar")

    return resultado
    