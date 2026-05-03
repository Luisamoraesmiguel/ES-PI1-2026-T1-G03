from conexao import conectar
import os
import mysql.connector

def zerezima():
    os.system('clear')  
    print("\n== ZEREZIMA ==")


    conexao = conectar()
    cursor = conexao.cursor()

    limpar = "DELETE FROM votos"
    cursor.execute(limpar)
    conexao.commit()

    relatorio = "SELECT Nome, Num_votacao FROM candidatos"
    cursor.execute(relatorio)
    lista_candidatos = cursor.fetchall() 
    print("Candidatos:")
    for candidato in lista_candidatos:
        print(f"Candidato: {candidato[0]} | Número: {candidato[1]} | Votos: 0")
    print("\nZerezima realizada com sucesso!")
    
    cursor.close() 
    conexao.close() 

    input("\nPressione Enter para liberar a urna")
    return True
