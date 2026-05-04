from conexao import conectar
from Criptografia import decifrar

def validar_identidade_eleitor(titulo, cpf_4digitos, chave):
    """
    Baseado na sua lógica de mesário, valida o eleitor para a urna.
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True) 
    
    
    sql = "SELECT nome, cpf, votou FROM eleitores WHERE titulo = %s AND chave_acesso = %s"
    cursor.execute(sql, (titulo, chave))
    eleitor = cursor.fetchone()

    if eleitor is None:
        cursor.close()
        conexao.close()
        return "INVALIDO" # Título ou chave errados
    
    
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