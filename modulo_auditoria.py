from conexao import conectar

def exibir_logs_ocorrencias():
    """RF002.02.01 / RF002.02.01.08: Lê e exibe o arquivo de texto de logs de forma direta"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DE LOGS DE OCORRÊNCIAS")
    print("="*60)
    
    try:
        arquivo = open("log_ocorrencias.txt", "r", encoding="utf-8")
        conteudo = arquivo.read()
        
        if not conteudo.strip():
            print("O arquivo de log está vazio por enquanto.")
        else:
            print(conteudo)
            
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo 'log_ocorrencias.txt' ainda não foi gerado pelo sistema.")
        
    print("="*60)

def exibir_protocolos_votacao():
    """RF002.02.02: Lista os protocolos em ordem alfabética (crescente) para conferência"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DOS PROTOCOLOS DE VOTAÇÃO")
    print("="*60)
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Busca todos os dados de votos de forma genérica
    cursor.execute("SELECT * FROM votos")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Nenhum protocolo de votação encontrado no banco.")
    else:
        protocolos = []
        for linha in resultados:
            # O protocolo criptografado costuma ser a última coluna da tabela votos
            protocolos.append(str(linha[-1]))
            
        # Garante o requisito do edital: listar os protocolos em ordem alfabética/crescente
        protocolos.sort()
        
        print("Nº    | CÓDIGO DO PROTOCOLO REGISTRADO (ORDENADO)")
        print("-"*55)
        for i, prot in enumerate(protocolos, 1):
            print(f"{i:<5} | {prot}")
            
    cursor.close()
    conexao.close()
    print("="*60)


if __name__ == "__main__":
    exibir_logs_ocorrencias()
    exibir_protocolos_votacao()