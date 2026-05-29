from Códigos_fonte import gerador_protocolo as protocolo
from conexao import conectar
from datetime import datetime
import random
import string
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Criptografia import cifrar

def gerar_protocolo(numero_candidato):
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    digitos = ''.join(random.choices(string.digits, k=5))
    candidato = str(numero_candidato).zfill(2)
    return f"V{letras}26{candidato}{digitos}"

def gravar_voto_no_banco(numero_escolhido, titulo_eleitor): 
    conexao = conectar()
    cursor = conexao.cursor()

    data_hora_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    protocolo_original = gerar_protocolo(numero_escolhido)
    protocolo_cifrado = cifrar(protocolo_original) 
    
    comando_sql = "INSERT INTO votos (Candidato, Datahora, protocolo_votacao) VALUES (%s, %s, %s)"
    cursor.execute(comando_sql, (numero_escolhido, data_hora_voto, protocolo_cifrado))

    sql_status = "UPDATE eleitores SET votou = 'S' WHERE titulo = %s"
    cursor.execute(sql_status, (titulo_eleitor,)) 
    
    conexao.commit()
    print("\nSucesso: Voto registrado!")

    cursor.close()
    conexao.close()

    return protocolo_original