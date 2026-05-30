import random
import string
from conexao import conectar
<<<<<<< HEAD
from Criptografia import cifrar
=======
from Códigos_fonte.validacoes.cpf import validar_cpf
from Códigos_fonte.validacoes.titulo import verificar_titulo

def cadastrar_eleitor():

    """
    Coleta os dados de um novo eleitor via terminal, valida o CPF
    e o título eleitoral, gera a chave de acesso, cifra o CPF
    e salva o registro no banco de dados.

    Args:
        Nenhum.

    Returns:
        None: Insere o eleitor no banco e exibe confirmação.
    """

    nome = input("Digite o nome completo do eleitor: ").upper().strip()
    titulo = ""
    cpf = ""
    votou = 'N'
    mesario = input("O eleitor é mesário? (S/N): ").upper().strip()

    while not validar_cpf(cpf):
        cpf = input ('Digite o CPF: ')
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, tente novamente.")
        else:
            from conexao import conectar
            from Criptografia import cifrar
            conexao = conectar()
            cursor = conexao.cursor()
            cpf_cifrado = cifrar(cpf)
            cursor.execute("SELECT cpf FROM eleitores WHERE cpf = %s", (cpf_cifrado,))
            if cursor.fetchone() is not None:
                print("\nCPF já cadastrado. Tente novamente.")
                cursor.close()
                conexao.close()
                cpf = ""
            else:
                cursor.close()
                conexao.close()
                break

    titulo_valido = False
    while not titulo_valido:
        titulo = input("Digite o número do título de eleitor: ")
        if verificar_titulo(titulo):
            titulo_valido = True
            print("Título de eleitor válido.")
        else:
            print("Título de eleitor inválido. Por favor, tente novamente.")

    senha = chave.gerar_chave(nome)
    senha_cifrada = Criptografia.cifrar(senha)

    print('Nome:', nome)
    print('Título:', titulo)
    print('CPF:', cpf)
    print('Mesário:', mesario)
    print('Senha:', senha)

    cpf_cifrado = Criptografia.cifrar(cpf)
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT cpf FROM eleitores WHERE cpf = %s", (cpf_cifrado,))
    if cursor.fetchone() is not None:
        print("\nCPF já cadastrado. Tente novamente.")
        cursor.close()
        conexao.close()
        return
    cursor.execute("SELECT titulo FROM eleitores WHERE titulo = %s", (titulo,))
    if cursor.fetchone() is not None:
        print("\nTítulo de eleitor já cadastrado. Tente novamente.")
        cursor.close()
        conexao.close()
        return
    sql = 'INSERT INTO eleitores (nome, cpf, titulo, mesario, votou, chave_de_acesso) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (nome, cpf_cifrado, titulo, mesario, 'N', senha_cifrada)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Eleitor cadastrado e criptografado com sucesso!")
    input("\nPressione Enter para continuar...")

>>>>>>> 5adc7d230dbf9a2dd01b9a993600021a7529052e

def cadastrar_candidato():
    print("\n" + "="*30)
    print(" CADASTRO DE CANDIDATO")
    print("="*30)

    nome = input("Nome do Candidato: ").upper().strip()
    partido = input("Partido: ").upper().strip()
    numero = input("Número de Votação: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    sql_check = "SELECT nome FROM candidatos WHERE Num_votacao = %s"
    cursor.execute(sql_check, (numero,))
    resultado = cursor.fetchone()

    if resultado:
        print("\n" + "!"*40)
        print(f"[ERRO] O número {numero} já pertence ao candidato {resultado[0]}.")
        print("Não é permitido duplicidade de números.")
        print("!"*40)
        input("\nPressione ENTER para voltar...")
        cursor.close()
        conexao.close()
        return

    try:
        sql_insert = "INSERT INTO candidatos (nome, partido, Num_votacao) VALUES (%s, %s, %s)"
        cursor.execute(sql_insert, (nome, partido, numero))
        conexao.commit()
        print("\n[SUCESSO] Candidato cadastrado com sucesso!")
        input("\nPressione ENTER para continuar...")
    except Exception as e:
        print(f"\n[ERRO] Falha ao acessar o banco: {e}")
        input("\nPressione ENTER para voltar...")

    cursor.close()
    conexao.close()

def cadastrar_eleitor():
    print("\n" + "="*30)
    print(" CADASTRO DE ELEITOR")
    print("="*30)
    
    nome = input("Nome completo: ").upper().strip()
    titulo = input("Título de eleitor: ").strip()
    cpf = input("CPF (somente números): ").strip()
    mesario = input("Atuará como mesário? (S/N): ").upper().strip()

    partes_nome = nome.split()
    letras_nome = partes_nome[0][:2]
    if len(partes_nome) > 1:
        letras_nome += partes_nome[1][0]
    else:
        letras_nome += "X"
    chave_aleatoria = ''.join(random.choices(string.digits, k=4))
    chave_acesso = letras_nome + chave_aleatoria

    conexao = conectar()
    cursor = conexao.cursor()
    
    try:
       
        sql = "INSERT INTO eleitores (nome, titulo, cpf, mesario, chave_de_acesso) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, titulo, cifrar(cpf), mesario, cifrar(chave_acesso)))
        conexao.commit()
        
        print("\n" + "-"*30)
        print(f"[SUCESSO] Eleitor {nome} cadastrado!")
        print(f"SUA CHAVE DE ACESSO É: {chave_acesso}")
        print("IMPORTANTE: Anote sua chave, ela não será mostrada novamente!")
        print("-"*30)
    except Exception as e:
        print(f"\n[ERRO] Falha ao cadastrar: {e}")
    finally:
        cursor.close()
        conexao.close()
        input("\nPressione Enter para continuar...")