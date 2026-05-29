from conexao import conectar
from Criptografia import decifrar

def validar_identidade_eleitor(titulo, cpf_4digitos, chave):
    
    """
    Valida a identidade do eleitor com base no título, nos 4 primeiros dígitos do CPF e na chave de acesso.

    Args:
        titulo (str): Número do título de eleitor.
        cpf_4digitos (str): Os 4 primeiros dígitos do CPF.
        chave (str): Chave de acesso única do eleitor.

    Returns:
        dict/str: Retorna o dicionário com os dados do eleitor se válido, ou uma string de erro ("INVALIDO", "JA_VOTOU", "CPF_ERRADO") caso contrário.
    """

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True) 
    
    
    sql = "SELECT nome, cpf, votou FROM eleitores WHERE titulo = %s AND chave_acesso = %s"
    cursor.execute(sql, (titulo, chave))
    eleitor = cursor.fetchone()

    if eleitor is None:
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    
    if eleitor['votou'] == 'S':
        cursor.close()
        conexao.close()
        return "JA_VOTOU"
    
    
    cpf_decifrado = decifrar(eleitor['cpf'])
    cpf_str = ''.join(filter(str.isdigit, str(cpf_decifrado)))
    
    if cpf_str[:4] == str(cpf_4digitos).strip():
        cursor.close()
        conexao.close()
        return eleitor # Retorna os dados para usar na urna
    else:
        cursor.close()
        conexao.close()
        return "CPF_ERRADO"
