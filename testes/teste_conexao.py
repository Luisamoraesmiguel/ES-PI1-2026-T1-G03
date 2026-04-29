import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='tabela_bd'
)

cursor = conexao.cursor()

sql = "INSERT INTO eleitores (nome, cpf, titulo, mesario, votou, chave_de_acesso) VALUES('João Silva', '12345678900', '123456789012', 'N', 'N', 'chave123')"
cursor.execute(sql)
conexao.commit()

print("Cadastrado com sucesso!")


