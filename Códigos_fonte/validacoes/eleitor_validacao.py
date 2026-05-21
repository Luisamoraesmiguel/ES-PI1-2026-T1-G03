from conexao import conectar
from Criptografia import cifrar, decifrar

def verificar_eleitor(titulo, cpf_4digitos, chave):
    conexao = conectar()
    cursor = conexao.cursor()
  
    sql = "SELECT nome, cpf, votou FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s "
    cursor.execute(sql, (titulo, chave))
    resultado = cursor.fetchone()

    
    if resultado is None:
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    # 3. Desempacota as variáveis (igual você fez com cpf, mesario = resultado)
    nome, cpf, votou = resultado

    
    if votou.upper() == 'S':
        cursor.close()
        conexao.close()
        return "JA_VOTOU"
    
    cpf_decifrado = decifrar(cpf)
   
    cpf_str = ''
    for c in str(cpf_decifrado):
        if c.isdigit():
            cpf_str += c
    cpf_4digitos = str(cpf_4digitos).strip()

    if cpf_str[:4] == cpf_4digitos:
        cursor.close()
        conexao.close()
   
        return (nome, cpf, votou) 
    else:
        cursor.close()
        conexao.close()
        return "CPF_ERRADO"
