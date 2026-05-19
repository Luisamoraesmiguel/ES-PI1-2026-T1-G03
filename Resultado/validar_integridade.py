from conexao import conectar
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def relatorio_integridade():
    
    conexao = conectar()
    cursor = conexao.cursor(buffered=True)

    cursor.execute("SELECT * FROM votos")
    total_votos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE votou = 'S'")
    total_eleitores = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    limpar_tela()
    print("\n==== RELATÓRIO DE INTEGRIDADE ====")
    print(f"Total de votos registrados: {total_votos}")
    print(f"Total de eleitores que votaram: {total_eleitores}")

    if total_votos == total_eleitores:
        print(f"\nA quantidade de votos confere perfeitamente")
    else:
        print(f"\nA quantidade de votos não confere com a quantidade de eleitores que votaram")

    input(f"\nPressione Enter para voltar...\n{'='*34}")