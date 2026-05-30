from conexao import conectar
import os
from conexao import conectar
import os

def zerezima():
    """
    Zera os votos do banco de dados e reinicia o status de votação
    de todos os eleitores, preparando a urna para uma nova eleição.
    Exibe a lista de candidatos com votos zerados ao final.

    Args:
        Nenhum.

    Returns:
        bool: True após a zerezima ser concluída com sucesso.
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n== ZERÉZIMA ==")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("TRUNCATE TABLE votos")
    conexao.commit()

    cursor.execute("UPDATE eleitores SET votou = 'N'")
    conexao.commit()

    cursor.execute("SELECT nome, num_votacao FROM candidatos")
    lista_candidatos = cursor.fetchall()

    print("\nCandidatos:")
    for nome, numero in lista_candidatos:
        print(f"  Candidato: {nome} | Número: {numero} | Votos: 0")

    print("\nZerézima realizada com sucesso!")

    cursor.close()
    conexao.close()

    input("\nPressione Enter para liberar a urna...")
    return True