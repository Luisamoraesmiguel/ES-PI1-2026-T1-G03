import os
# Importação absoluta a partir da raiz do projeto
from Códigos_fonte.conexao import conectar
from Votacao.log import exibir_logs

def consultar_auditoria():
    # Abre a conexão com o banco de dados
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
 
    caminho_log_txt = "log_ocorrencias.txt"
  
    with open(caminho_log_txt, "a", encoding="utf-8") as arquivo:
        print("\n" + "="*60)
        print("RELATÓRIO DE AUDITORIA")
        print("="*60)

        if not resultados:
            print("Nenhum voto encontrado no banco de dados.")
        else:
            for linha in resultados:
                # Formata a linha para o log (removendo caracteres extras)
                conteudo = str(linha).replace("(", "").replace(")", "").replace("'", "")
                texto_log = "[REGISTRO DE VOTO]: " + conteudo
                
                print(texto_log)
                arquivo.write(texto_log + "\n")

    cursor.close()
    conexao.close()
    
    print("\n" + "="*60)
    print("Sucesso! Os registros de auditoria foram adicionados ao log.")

if __name__ == "__main__":
    consultar_auditoria()
    exibir_logs()