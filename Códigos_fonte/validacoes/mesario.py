import mysql.connector
from Criptografia import cifrar

def verificar_mesario(titulo, cpf_4digitos, chave):
    
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='', # Se tiver senha, coloque aqui
        database='tabela_bd'
    )   
    cursor = conexao.cursor()
    
    # Comando SQL para verificar se o mesário existe no banco de dados
    sql = f"SELECT cpf, mesario FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s "
    
    cursor.execute(sql, (titulo, chave)) # Executa o comando SQL
    resultado = cursor.fetchone() # Pega o resultado da consulta

    if resultado:
        cpf_banco, is_mesario = resultado # Pega o CPF e se é mesário do resultado
        if is_mesario != 'S': # Verifica se é mesário
            print('Acesso negado: O título fornecido não pertence a um mesário.')
            return False
        cpf_banco_str = str(cpf_banco) # Converte o CPF do banco de dados para string
        if cpf_banco_str.endwith(str(cpf_4digitos)): # Verifica se os 4 últimos dígitos do CPF no banco de dados correspondem aos 4 dígitos fornecidos pelo usuário
            print('Acesso concedido: Mesário verificado com sucesso.')
            return True
        else:
            print('Cpf invalido.')
            return False
    else:
        print('Título ou chave de acesso inválidos.')
        return False
    
 

    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados
    
    if resultado:
        cpf_banco = resultado[0] # Pega o CPF do resultado
        CPF_4_CIFRADO = cifrar(cpf_4digitos) # Cifra os 4 últimos dígitos do CPF fornecido pelo usuário
       
    if str(cpf_banco).endswith(str(CPF_4_CIFRADO)): # Verifica se os 4 últimos dígitos do CPF no banco de dados correspondem aos 4 dígitos fornecidos pelo usuário
        return True
        
        
        
    return False

    #if resultado and resultado[0] == 'S': # Verifica se o mesário existe e é um mesário
        #return True
    #else:
        #return False