from conexao import conectar
import os
import mysql.connector

def zerezima():
    os.system('clear')  # Limpa a tela para melhor visualização
    print("\n== ZEREZIMA ==")


    conexao = conectar()
    cursor = conexao.cursor()

    #Zerando os votos dos candidatos
    limpar = "DELETE FROM votos"
    cursor.execute(limpar)
    conexao.commit()

    relatorio = "SELECT Nome, Num_votacao FROM candidatos"
    cursor.execute(relatorio)
    lista_candidatos = cursor.fetchall() # Pega a lista de candidatos para o relatório
    print("Candidatos:")
    for candidato in lista_candidatos:
        print(f"Candidato: {candidato[0]} | Número: {candidato[1]} | Votos: 0")
    print("\nZerezima realizada com sucesso!")
    
    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados

    input("\nPressione Enter para liberar a urna")
    return True