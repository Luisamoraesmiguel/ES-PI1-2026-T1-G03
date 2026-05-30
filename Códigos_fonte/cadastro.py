import random
import string
from conexao import conectar
from Criptografia import cifrar

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