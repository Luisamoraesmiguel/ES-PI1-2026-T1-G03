import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)
cursor = conexao.cursor()

sql = "INSERT INTO eleitores (nome, cpf, titulo, mesario, votou, chave_de_acesso) VALUES (%s, %s, %s, %s, %s, %s)"
valores = ("João Silva", "12345678900", "123456789012", 'N', 'N', 'chave123')
cursor.execute(sql, valores)
conexao.commit()

print("Cadastrado com sucesso!")

    
    







