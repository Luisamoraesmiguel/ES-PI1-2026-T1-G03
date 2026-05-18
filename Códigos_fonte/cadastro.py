import Criptografia
from Códigos_fonte import chave
from conexao import conectar
from Códigos_fonte.validacoes.cpf import validar_cpf
from Códigos_fonte.validacoes.titulo import verificar_titulo

def cadastrar_eleitor():
    nome = input("Digite o nome completo do eleitor: ").upper().strip()
    titulo = ""
    cpf = ""
    votou = 'N'
    mesario = input("O eleitor é mesário? (S/N): ").upper().strip()

    while not validar_cpf(cpf):
        cpf = input("Digite o CPF do eleitor (apenas números): ")
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, tente novamente.")

    titulo_valido = False
    while not titulo_valido:
        titulo = input("Digite o número do título de eleitor: ")
        if verificar_titulo(titulo):
            titulo_valido = True
            print("Título de eleitor válido.")
        else:
            print("Título de eleitor inválido. Por favor, tente novamente.")

    senha = chave.gerar_chave(nome)

    print('Nome:', nome)
    print('Título:', titulo)
    print('CPF:', cpf)
    print('Mesário:', mesario)
    print('Senha:', senha)

    cpf_cifrado = Criptografia.cifrar(cpf)
    
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'INSERT INTO eleitores (nome, cpf, titulo, mesario, votou, chave_de_acesso) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (nome, cpf_cifrado, titulo, mesario, 'N', senha)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Eleitor cadastrado e criptografado com sucesso!")


def cadastrar_candidato():
    nome = input("Digite o nome do candidato: ")
    partido = input("Digite o partido do candidato: ")
    numero = input("Digite o número do candidato: ")

    while not numero.isdigit():
        print("Digite o número do candidato com apenas dígitos ")
        numero = int('Digite o número do candidato: ')

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT numero FROM candidatos WHERE numero = %s", (numero,))
    if cursor.fetchone() is not None:
        print("Número de candidato já existe. Tente novamente.")
        cursor.close()
        conexao.close()
        return


    sql = 'INSERT INTO candidatos ( nome, partido, numero) VALUES (%s, %s, %s)'
    valores = (nome, partido, numero)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Candidato cadastrado com sucesso!")
    cursor.close()
    conexao.close()

