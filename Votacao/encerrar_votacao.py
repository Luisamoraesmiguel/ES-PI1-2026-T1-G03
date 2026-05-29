import mysql.connector
from conexao import conectar

def executar_encerramento_logica():

    """
    Valida as credenciais do mesário para autorizar o encerramento da votação e consolidar os resultados.

    Args:
        Nenhum.

    Returns:
        bool: Retorna True se a votação for encerrada com sucesso, False caso contrário.
    """

    conn = conectar()
    cursor = conn.cursor()

    titulo = input("Título do Eleitor: ")
    cpf_parcial = input("4 primeiros dígitos do CPF: ")
    chave = input("Chave de acesso do mesário: ")

    query = "SELECT chave_de_acesso FROM eleitores WHERE titulo = %s AND LEFT(cpf, 4) = %s AND mesario = 'S'"
    cursor.execute(query, (titulo, cpf_parcial))
    resultado = cursor.fetchone()

    if resultado and resultado[0] == chave:
        confirmacao = input("Deseja realmente encerrar a votação? (Sim/Não): ").strip().lower()

        if confirmacao == 'sim':
            segunda_chave = input("Digite novamente a chave de acesso do mesário: ")
            
            if segunda_chave == chave:
                query_consolidar = """
                    SELECT c.Nome, COUNT(v.Id) 
                    FROM candidatos c 
                    LEFT JOIN votos v ON c.Id = v.Candidato 
                    GROUP BY c.Id, c.Nome
                """
                cursor.execute(query_consolidar)
                resultados = cursor.fetchall()

                print("\n--- RESULTADOS CONSOLIDADOS ---")
                for nome, total in resultados:
                    print(f"Candidato: {nome} | Votos: {total}")
                    
                    from log import registrar_log
                    registrar_log(f"ENCERRAMENTO: Votação finalizada com sucesso! ")

                cursor.close()
                conn.close()
                return True
            else:
                print("Chave de confirmação incorreta.")
        else:
            print("Encerrar cancelado.")
    else:
        print("Dados inválidos ou usuário não é mesário.")

    cursor.close()
    conn.close()
    return False