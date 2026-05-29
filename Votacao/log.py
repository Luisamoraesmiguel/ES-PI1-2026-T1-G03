from datetime import datetime

ARQUIVO_LOG = "log_ocorrencias.txt"

def registrar_log(mensagem):

    """
    Grava um registro de evento com carimbo de data e hora no arquivo de log de ocorrências.

    Args:
        mensagem (str): O texto com a descrição do evento a ser registrado.

    Returns:
        None: Não possui retorno de valor.
    """

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {mensagem}\n"
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(linha)

def exibir_logs():

    """
    Lê e imprime na tela todos os registros armazenados no arquivo de logs de ocorrências.

    Args:
        Nenhum.

    Returns:
        None: Não possui retorno de valor.
    """

    print("\n=== LOG DE OCORRÊNCIAS ===")
    try:
        with open(ARQUIVO_LOG, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum log encontrado.")