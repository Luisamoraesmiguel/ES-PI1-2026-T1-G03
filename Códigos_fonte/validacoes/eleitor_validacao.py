from conexao import conectar
from Criptografia import cifrar, decifrar

def verificar_eleitor(titulo, cpf_4digitos, chave):
    """ 
    Verifica se um eleitor possui acesso válido ao sistema de votação. 
    
    Args: 
        titulo (str): Número do título de eleitor informado. 
        cpf_4digitos (str | int): Quatro primeiros dígitos do CPF utilizados para validação. 
        chave (str): Chave de acesso do eleitor. 

    Returns: 
        tuple | str: Retorna uma tupla contendo nome, CPF e status de votação caso os dados sejam válidos. Retorna "INVALIDO", "JA_VOTOU" ou "CPF_ERRADO" em caso de falha. 
   
    """
    conexao = conectar()
    cursor = conexao.cursor()
  
    sql = "SELECT nome, cpf, votou FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s "
    cursor.execute(sql, (titulo, cifrar(chave)))
    resultado = cursor.fetchone()

    
    if resultado is None:
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    nome, cpf, votou = resultado

    
    if votou.upper() == 'S':
        cursor.close()
        conexao.close()
        return "JA_VOTOU"
    
    cpf_decifrado = decifrar(cpf)
    cpf_decifrado = decifrar(cpf)
    
   
    cpf_str = ''
    for c in str(cpf_decifrado): 
        if c.isalpha():
            cpf_str += str(ord(c) - ord('A'))
    cpf_4digitos = str(cpf_4digitos).strip()

    if cpf_str[:4] == cpf_4digitos:
        cursor.close()
        conexao.close()
   
        return (nome, cpf, votou) 
    else:
        cursor.close()
        conexao.close()
        return "CPF_ERRADO"
