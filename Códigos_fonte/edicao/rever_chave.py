from conexao import conectar
from Criptografia import decifrar
def rever_chave_acesso():
    titulo = input("Digite o título do eleitor: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT chave_de_acesso FROM eleitores WHERE titulo = %s", (titulo,))
    resultado = cursor.fetchone() 
    if resultado:
        chave_de_acesso = resultado[0]
        chave_de_acesso = decifrar(chave_de_acesso)
        letras = chave_de_acesso[:3]
        numeros = ''.join(str(ord(c) - ord('A')) for c in chave_de_acesso[3:7]) # Converte as letras restantes para números
        print(f"A chave de acesso do eleitor com título {titulo} é: {letras}{numeros}")
    
    else:
        print("Eleitor não encontrado.")
    cursor.close()
    conexao.close()

