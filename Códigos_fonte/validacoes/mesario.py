from conexao import conectar
from Criptografia import decifrar


def verificar_mesario(titulo, cpf_4digitos, chave):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = "SELECT cpf, mesario FROM eleitores WHERE titulo = %s AND chave_de_acesso = %s "
    cursor.execute(sql, (titulo, chave))
    resultado = cursor.fetchone()

    if resultado is None:
        print("\n[ERRO] Título ou chave de acesso incorretos. Tente novamente.")
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    cpf, mesario = resultado

    if mesario.upper() == 'N':
        print("\n[ERRO] O eleitor com este título não é um mesário. Tente novamente.")
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
    cpf_decifrado = decifrar(cpf)
   

    cpf_str = ''
    for c in str(cpf_decifrado):
        numero = str(ord(c) - ord('A'))
        cpf_str += numero
    cpf_4digitos = str(cpf_4digitos).strip() 



    if cpf_str[:4] == cpf_4digitos:
        cursor.close()
        conexao.close()
        return {"nome": titulo} 
    else:
        print(f"\n[ERRO] CPF incorreto. Tente novamente.{cpf_decifrado}")
        cursor.close()
        conexao.close()
        return "INVALIDO"
    
