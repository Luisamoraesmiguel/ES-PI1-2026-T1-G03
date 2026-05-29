import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexao import conectar

def consultar_auditoria():
    """
    Consulta todos os votos registrados no banco de dados e gera um
    arquivo de log com os registros encontrados.

    Args:
        Nenhum.

    Returns:
        None: Exibe os registros no terminal e salva em 'log_ocorrencias.txt'.
    """
    conexao = conectar()
    cursor = conexao.cursor() 

    cursor.execute("SELECT * FROM votos")
    resultados = cursor.fetchall()

    arquivo = open("log_ocorrencias.txt", "w", encoding="utf-8")

    print("\n" + "="*60)
    print("RELATÓRIO DE AUDITORIA")
    print("="*60)

    if not resultados:
        print("Nenhum voto encontrado.")
    else:
        for linha in resultados:
            # transformamos a linha toda em texto
            # ele vai imprimir todas as colunas
            conteudo = str(linha).replace("(", "").replace(")", "").replace("'", "")
            
            texto_log = "[REGISTRO]: " + conteudo
            
            print(texto_log)
            arquivo.write(texto_log + "\n")

    arquivo.close()
    cursor.close()
    conexao.close()
    
    print("\n" + "="*60)
    print("Sucesso! O arquivo .txt foi gerado.")

consultar_auditoria()