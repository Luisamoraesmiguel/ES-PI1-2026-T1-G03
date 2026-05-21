from conexao import conectar
import os
import mysql.connector

def zerezima():
    os.system('cls')  
    print("\n== ZEREZIMA ==")


    conexao = conectar()
    cursor = conexao.cursor()

    limpar = "DELETE FROM votos"
    cursor.execute(limpar)
    conexao.commit()

    resetar_votacao = "UPDATE eleitores SET votou = N"
    cursor.execute(resetar_votacao)

    relatorio = "SELECT Nome, Num_votacao FROM candidatos"
    cursor.execute(relatorio)
    lista_candidatos = cursor.fetchall() 
    print("Candidatos:")
    for candidato in lista_candidatos:
        print(f"\nCandidato: {candidato[0]} | Número: {candidato[1]} | Votos: 0")
    print("\nZerezima realizada com sucesso!")
    
    cursor.close() 
    conexao.close() 

    input("\nPressione Enter para liberar a urna")
    return True
