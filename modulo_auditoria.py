from conexao import conectar

def exibir_logs_ocorrencias():
    """RF002.02.01: Lê e exibe o arquivo de texto de logs"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DE LOGS DE OCORRÊNCIAS (HISTÓRICO CRÍTICO)")
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
        print("O arquivo 'log_ocorrencias.txt' ainda não foi criado.")
    print("="*60)

def exibir_protocolos_votacao():
    """RF002.02.02: Lista os protocolos puxando os dados de forma segura"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DOS PROTOCOLOS DE VOTAÇÃO")
    print("="*60)
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Usamos * para evitar o erro de coluna 'Unknown column' no seu banco local
    cursor.execute("SELECT * FROM votos")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Nenhum protocolo de votação encontrado no banco.")
    else:
        print("Nº    | CÓDIGO DO PROTOCOLO REGISTRADO")
        print("-"*45)
        for i, linha in enumerate(resultados, 1):
            # linha[-1] pega o último campo da tabela votos, que é o Protocolo_votacao
            print(f"{i}     | {linha[-1]}")
            
    cursor.close()
    conexao.close()
    print("="*60)

# CHAMADA DOS TESTES
exibir_logs_ocorrencias()
exibir_protocolos_votacao()