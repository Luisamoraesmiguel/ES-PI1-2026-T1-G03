from conexao import conectar

def exibir_logs_ocorrencias():
    """RF002.02.01: Lê e exibe o arquivo de texto de logs"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DE LOGS DE OCORRÊNCIAS (HISTÓRICO CRÍTICO)")
    print("="*60)
    
    arquivo = open("log_ocorrencias.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()
    
    if not conteudo.strip():
        print("O arquivo de log está vazio por enquanto.")
    else:
        print(conteudo)
        
    arquivo.close()
    print("="*60)

def exibir_protocolos_votacao():
    """RF002.02.02: Lista os protocolos em ordem usando a coluna correta"""
    print("\n" + "="*60)
    print("EXIBIÇÃO DOS PROTOCOLOS DE VOTAÇÃO")
    print("="*60)
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    # IMPORTANTE: Busca a coluna real 'Protocolo_votacao' da tabela 'votos'
    cursor.execute("SELECT Protocolo_votacao FROM votos ORDER BY Protocolo_votacao ASC")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Nenhum protocolo de votação encontrado no banco.")
    else:
        print("Nº    | CÓDIGO DO PROTOCOLO")
        print("-"*35)
        for i, linha in enumerate(resultados, 1):
            print(f"{i}     | {linha[0]}")
            
    cursor.close()
    conexao.close()
    print("="*60)

# CHAMADA DE TESTE (Pronto para rodar!)
exibir_logs_ocorrencias()
exibir_protocolos_votacao()