from conexao import conectar

def estatistica_comparecimento():
    """
    Calcula e exibe a estatística de comparecimento da eleição,
    mostrando o total de eleitores aptos, quantos votaram
    e o percentual de participação.

    Args:
        Nenhum.

    Returns:
        None: Imprime as estatísticas no terminal.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE votou = 'S'")
    votaram = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    percentual = (votaram / total * 100) if total > 0 else 0

    print("\n== ESTATÍSTICA DE COMPARECIMENTO ==")
    print(f"Eleitores aptos: {total}")
    print(f"Total de eleitores votantes: {votaram}")
    print(f"Percentual de participação: {percentual:.2f}%")
    input("\nPressione Enter para continuar...")