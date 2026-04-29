from conexao import conectar
import mysql.connector

def cadastrar_eleitor(nome, cpf_cifrado, titulo, mesario, votou, senha):
    """
    Funcao que envia os dados do eleitor para o banco de dados.

    Args:
        nome (str): Nome do eleitor.
        titulo (str): Numero do titulo.
        cpf (str): Numero do CPF.

    Returns:
        int: Retorna 1 se deu certo ou 0 se deu erro.
    """
    #try:
        # Tenta conectar ao banco de dados
    #conexao = mysql.connector.connect(
        #host="localhost",
       #user="root",
        #password="sabrina9728", # Se tiver senha, coloque aqui
        #database="tabela_bd"
    
    conexao = conectar()
    cursor = conexao.cursor()

        # Comando para inserir os dados na tabela
    sql = 'INSERT INTO eleitores ( nome, cpf, titulo, mesario, votou, chave_de_acesso) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (nome, cpf_cifrado, titulo, mesario, 'N', senha )

    
    cursor.execute(sql, valores)
    conexao.commit() 
    
    cursor.close() # Fecha o cursor
    conexao.close()
    
    print("Cadastro realizado!")
    return 1

    #except Exception as erro:
        #print(f"Erro: {erro}")
        #return 0

    #finally:
        # Fecha a conexao para nao travar o banco
        #if 'conexao' in locals() and conexao.is_connected():
            #cursor.close()
            #conexao.close()


def cadastrar_candidato():
    nome = input("Digite o nome do candidato: ")
    partido = input("Digite o partido do candidato: ")
    numero = input("Digite o número do candidato: ")

    while not numero.isdigit():
        print("Digite o número do candidato com apenas dígitos ")
        numero = int('Digite o número do candidato: ')

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT numero FROM candidatos WHERE numero = %s", (numero,))
    if cursor.fetchone() is not None:
        print("Número de candidato já existe. Tente novamente.")
        cursor.close()
        conexao.close()
        return


    sql = 'INSERT INTO candidatos ( nome, partido, numero) VALUES (%s, %s, %s)'
    valores = (nome, partido, numero)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Candidato cadastrado com sucesso!")
    cursor.close()
    conexao.close()

