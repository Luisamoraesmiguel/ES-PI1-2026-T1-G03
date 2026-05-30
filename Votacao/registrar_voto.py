from Códigos_fonte import gerador_protocolo as protocolo
from conexao import conectar
from datetime import datetime
import random
import string
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Criptografia import cifrar

def gerar_protocolo(numero_candidato):

    """
    Gera um protocolo de votação no padrão estabelecido (V + 2 letras + '26' + Candidato + 5 dígitos).

    Args:
        numero_candidato (str/int): O número de votação do candidato escolhido.

    Returns:
        str: O protocolo gerado em texto claro.
    """

    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    digitos = ''.join(random.choices(string.digits, k=5))
    candidato = str(numero_candidato).zfill(2)
    return f"V{letras}26{candidato}{digitos}"

def gravar_voto_no_banco(numero_escolhido, titulo_eleitor): 

    """
    Grava o voto do candidato no banco de dados com protocolo cifrado e atualiza o status do eleitor para 'votou'.

    Args:
        numero_escolhido (str/int): O número de votação do candidato.
        titulo_eleitor (str): O título de eleitor do votante.

    Returns:
        str: Retorna o protocolo original gerado em formato limpo.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    
    cursor.execute("SELECT Id FROM candidatos WHERE Num_votacao = %s", (numero_escolhido,))
    resultado_id = cursor.fetchone()
    
    if resultado_id:
        id_verdadeiro = resultado_id[0]
    else:
        
        id_verdadeiro = None 

    data_hora_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    protocolo_original = gerar_protocolo(numero_escolhido)
    protocolo_cifrado = cifrar(protocolo_original) 
    
   
    comando_sql = "INSERT INTO votos (Candidato, Datahora, protocolo_votacao) VALUES (%s, %s, %s)"
    cursor.execute(comando_sql, (id_verdadeiro, data_hora_voto, protocolo_cifrado))

    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) 
    
    conexao.commit()

    cursor.close()
    conexao.close()

    return protocolo_original