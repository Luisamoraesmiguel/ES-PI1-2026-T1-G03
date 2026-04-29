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
    # 1. Limpeza do dado
    termo = dado.strip()

    # 2. Obtendo a conexão e o cursor (precisa dos parênteses '()')
    # Usamos dictionary=True para facilitar a leitura dos resultados
    conexao = conectar() 
    cursor = conexao.cursor(dictionary=True)

    # 3. Lógica de Criptografia (CPF vs Título)
    if len(termo) == 11:
        termo_pesquisa = Criptografia.cifrar(termo)
        campo_sql = "cpf"
    else:
        termo_pesquisa = termo
        campo_sql = "titulo"

    # 4. Preparação da Query
    query = f"SELECT nome, cpf, titulo, mesario FROM eleitores WHERE {campo_sql} = %s"

    # 5. Execução direta (Sem TRY)
    cursor.execute(query, (termo_pesquisa,))
    resultado = cursor.fetchone()

    # 6. Exibição dos resultados
    if resultado:
        print("\n" + "="*30)
        print("   ELEITOR ENCONTRADO")
        print("="*30)
        print(f"NOME:    {resultado['nome']}")
        print(f"TÍTULO:  {resultado['titulo']}")
        print(f"MESÁRIO: {'SIM' if resultado['mesario'] else 'NÃO'}")
        print("="*30 + "\n")
    else:
        print("\n" + "="*30)
        print("   ELEITOR NÃO ENCONTRADO")
        print("="*30 + "\n")

    # 7. Fechamento manual (Já que não temos o 'finally')
    cursor.close()
    conexao.close()

    return resultado