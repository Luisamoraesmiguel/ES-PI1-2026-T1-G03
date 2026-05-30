from conexao import conectar
from Criptografia import decifrar

def exibir_protocolos():
    """
    Busca e exibe todos os protocolos de votação registrados no banco,
    descriptografando cada um antes de exibir.

    Args:
        Nenhum.

    Returns:
        None: Imprime os protocolos descriptografados no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT protocolo_votacao FROM votos ORDER BY Id ASC")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    print("\n== PROTOCOLOS DE VOTAÇÃO ==")

    if not resultados:
        print("Nenhum protocolo registrado.")
    else:
        for i, (protocolo,) in enumerate(resultados, start=1):
            protocolo_decifrado = decifrar(protocolo)
            print(f"{i}. {protocolo_decifrado}")

    input("\nPressione Enter para continuar...")