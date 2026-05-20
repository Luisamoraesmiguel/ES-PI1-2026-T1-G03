from conexao import conectar
from Criptografia import decifrar

def exibir_protocolos():
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