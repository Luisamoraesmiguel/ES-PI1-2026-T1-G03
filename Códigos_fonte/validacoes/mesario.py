from conexao import conectar
from Criptografia import cifrar, decifrar

def verificar_mesario(titulo, cpf_4digitos, chave):
    """ 
    Verifica se um usuário é autorizado como mesário no sistema. 
    
    Args: 
        titulo (str): Número do título de eleitor informado. cpf_4digitos (str | int): Quatro primeiros dígitos do CPF para conferência. chave (str): Chave de acesso do usuário. 
        
    Returns: 
        dict | str: Retorna um dicionário contendo o nome do mesário autorizado ou as mensagens "INVALIDO", "NAO_AUTORIZADO" ou "CPF_INCORRETO". 
    
    """
    conexao = conectar()
    cursor = conexao.cursor()
    

    sql = "SELECT nome, cpf, mesario FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s"
    cursor.execute(sql, (titulo, cifrar(chave)))
    resultado = cursor.fetchone()

    if resultado is None:
        cursor.close()
        conexao.close()
        return "INVALIDO" 
    
    nome_db, cpf_banco, mesario_status = resultado

    if mesario_status.upper() == 'N':
        cursor.close()
        conexao.close()
        return "NAO_AUTORIZADO"
    
    cpf_decifrado = decifrar(cpf_banco)
    
    cpf_str = ''
    for c in str(cpf_decifrado):
        numero = str(ord(c) - ord('A'))
        cpf_str += numero
    
    cpf_4digitos = str(cpf_4digitos).strip() 


    if cpf_str[:4] == cpf_4digitos:
        cursor.close()
        conexao.close()
        return {"nome": nome_db}
    else:
        cursor.close()
        conexao.close()
        return "CPF_INCORRETO"