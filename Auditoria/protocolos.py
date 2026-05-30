from conexao import conectar
from Criptografia import decifrar, _letra_para_digito

def descriptografar_protocolo(protocolo_cifrado):
    """
    Descriptografa um protocolo de votação utilizando a Cifra de Hill.

    Args:
        protocolo_cifrado (str): Protocolo criptografado a ser descriptografado.

    Returns:
        str: Protocolo descriptografado, pronto para exibição ou análise.
    """
    flags = [False, False, False, True, True, True, True, True, True, True, True, True]
    texto_decifrado = decifrar(protocolo_cifrado)
    resultado = []
    for i, c in enumerate(texto_decifrado):
        resultado.append(_letra_para_digito(c, flags[i]))
    return ''.join(resultado)


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

    cursor.execute("SELECT protocolo_votacao FROM votos ")
    resultados = cursor.fetchall()
    resultados_decifrados = sorted([descriptografar_protocolo(p) for (p,) in resultados]) 

    cursor.close()
    conexao.close()

    print("\n== PROTOCOLOS DE VOTAÇÃO ==")

    if not resultados:
        print("Nenhum protocolo registrado.")
    else:
        for i, protocolo in enumerate(resultados_decifrados, start=1):

            print(f"{i}. {protocolo}")

    input("\nPressione Enter para continuar...")