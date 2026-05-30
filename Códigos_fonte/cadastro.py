import Criptografia
import Códigos_fonte.chave as chave
from conexao import conectar
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


def cadastrar_candidato():

    """
    Coleta os dados de um novo candidato via terminal, verifica se
    o número de votação já existe no banco e, se não existir,
    salva o registro.

    Args:
        Nenhum.

    Returns:
        None: Insere o candidato no banco e exibe confirmação,
              ou avisa se o número já estiver em uso.
    """
    
    nome = input("Digite o nome do candidato: ").upper().strip()    
    partido = input("Digite o partido do candidato: ").upper().strip()
    numero = input("Digite o número do candidato: ")

    while not numero.isdigit():
        print("Digite o número do candidato com apenas dígitos ")
        numero = int('Digite o número do candidato: ')

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT num_votacao FROM candidatos WHERE num_votacao = %s", (numero,)) 
    if cursor.fetchone() is not None:
        print("\nNúmero de candidato já existe. Tente novamente.")
        cursor.close()
        conexao.close()
        return


    sql = 'INSERT INTO candidatos ( nome, partido, num_votacao) VALUES (%s, %s, %s)'
    valores = (nome, partido, numero)
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nCandidato cadastrado com sucesso!")
    input("\nPressione Enter para continuar...")
    cursor.close()
    conexao.close()

