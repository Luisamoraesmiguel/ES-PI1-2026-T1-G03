def zerezima():
    os.system('clear')  # Limpa a tela para melhor visualização
    print("\n== ZEREZIMA ==")

    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='tabela_bd'
    )

    cursor = conexao.cursor()

    #Zerando os votos dos candidatos
    limpar = "UPDATE candidatos SET votos = 0"
    cursor.execute(limpar)
    conexao.commit()

    relatorio = "SELECT nome FROM candidatos"
    cursor.execute(relatorio)
    lista_candidatos = cursor.fetchall() # Pega a lista de candidatos para o relatório
    print("Candidatos:")
    for candidato in lista_candidatos:
        print(f"Candidato: {candidato[0]} | Votos: {candidato[1]}")
    print("\nZerezima realizada com sucesso!")
    
    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados

    input("\nPressione Enter para liberar a urna")