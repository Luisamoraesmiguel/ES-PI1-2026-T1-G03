import random
import string
from conexao import conectar
from Criptografia import cifrar
from Códigos_fonte.validacoes.cpf import validar_cpf
from Códigos_fonte.validacoes.titulo import verificar_titulo

def cadastrar_candidato():
    print("\n" + "="*30)
    print(" CADASTRO DE CANDIDATO")
    print("="*30)
    nome = input("Nome do Candidato: ").upper().strip()
    partido = input("Partido: ").upper().strip()
    numero = input("Número de Votação: ").strip()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM candidatos WHERE Num_votacao = %s", (numero,))
    if cursor.fetchone():
        print(f"\n[ERRO] O número {numero} já está em uso.")
        input("\nPressione ENTER para voltar...")
        cursor.close()
        conexao.close()
        return
    try:
        cursor.execute("INSERT INTO candidatos (nome, partido, Num_votacao) VALUES (%s, %s, %s)", (nome, partido, numero))
        conexao.commit()
        print("\n[SUCESSO] Candidato cadastrado!")
    except Exception as e:
        print(f"\n[ERRO] {e}")
    finally:
        cursor.close()
        conexao.close()
        input("\nPressione ENTER para continuar...")

def cadastrar_eleitor():
    print("\n" + "="*30)
    print(" CADASTRO DE ELEITOR")
    print("="*30)
    nome = input("Nome completo: ").upper().strip()
    titulo = input("Título de eleitor: ").strip()
    
    # Chama a validação matemática do Título (Requisito Anexo A)
    if not verificar_titulo(titulo):
        print("[ERRO] Título de eleitor inválido.")
        input("Pressione Enter para voltar...")
        return

    cpf = input("CPF (somente números): ").strip()
    # Chama a validação matemática do CPF (Requisito Anexo B)
    if not validar_cpf(cpf):
        print("[ERRO] CPF inválido.")
        input("Pressione Enter para voltar...")
        return

    mesario = input("Atuará como mesário? (S/N): ").upper().strip()
    
    # Gerar Chave de Acesso (Requisito pág 14)
    partes = nome.split()
    chave_prefixo = partes[0][:2] + (partes[1][0] if len(partes) > 1 else "X")
    chave_acesso = chave_prefixo + ''.join(random.choices(string.digits, k=4))
    
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO eleitores (nome, titulo, cpf, mesario, chave_de_acesso, votou) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (nome, titulo, cifrar(cpf), mesario, cifrar(chave_acesso), 'N'))
        conexao.commit()
        print(f"\n[SUCESSO] Eleitor cadastrado! Chave: {chave_acesso}")
    except Exception as e:
        print(f"\n[ERRO] {e}")
    finally:
        cursor.close()
        conexao.close()
        input("\nPressione Enter para continuar...")

def editar_candidato():
    print("\n== EDIÇÃO DE CANDIDATO ==")
    numero = input("Digite o número do candidato que deseja editar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM candidatos WHERE Num_votacao = %s", (numero,))
    candidato = cursor.fetchone()
    if candidato is None:
        print("[ERRO] Candidato não encontrado.")
        input("\nPressione Enter para voltar...")
        cursor.close()
        conexao.close()
        return
    print(f"\nCandidato encontrado: {candidato[1]}")
    print("1- Nome\n2- Número\n3- Partido\n0- Voltar")
    opcao = input("Escolha: ")
    if opcao == "1":
        novo = input("Novo nome: ")
        cursor.execute("UPDATE candidatos SET Nome = %s WHERE Num_votacao = %s", (novo, numero))
    elif opcao == "2":
        novo = input("Novo número: ")
        cursor.execute("SELECT Nome FROM candidatos WHERE Num_votacao = %s", (novo,))
        if cursor.fetchone():
            print(f"\n[ERRO] O número {novo} já está em uso.")
            input("\nPressione ENTER para voltar...")
            cursor.close()
            conexao.close()
            return
        cursor.execute("UPDATE candidatos SET Num_votacao = %s WHERE Num_votacao = %s", (novo, numero))
    elif opcao == "3":
        novo = input("Novo partido: ")
        cursor.execute("UPDATE candidatos SET Partido = %s WHERE Num_votacao = %s", (novo, numero))
    elif opcao == "0":
        cursor.close()
        conexao.close()
        return
    conexao.commit()
    print("\nCandidato atualizado com sucesso!")
    input("\nPressione Enter para concluir...")
    cursor.close()
    conexao.close()