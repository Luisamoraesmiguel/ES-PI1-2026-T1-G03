import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)
cursor = mydb.cursor()

cpf = str(input("Digite o CPF: "))
nome = str(input("Digite o nome: "))
cursor.execute(f"INSERT into teste (cpf, nome) VALUES ('{cpf}', '{nome}')")
mydb.commit()
cursor.execute("select * from teste")
table = cursor.fetchall()
print(table)
