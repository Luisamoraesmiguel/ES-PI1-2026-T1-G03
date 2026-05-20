from Códigos_fonte.edicao.remover_eleitor import apagar_eleitor_do_banco as remover_eleitor
from Códigos_fonte.edicao.eleitor import editar_eleitor
from Códigos_fonte.edicao.candidato import editar_candidato
from Códigos_fonte.edicao.rever_chave import rever_chave_acesso
from Códigos_fonte.edicao.busca_eleitor import buscar_eleitor as buscar, buscar_candidato
from Códigos_fonte.cadastro import cadastrar_candidato, cadastrar_eleitor
from Votacao.Abertura import abertura_votacao
from Criptografia import cifrar
from Resultado.vts_partido import votos_por_partido
from Resultado.vts_candidato import votos_por_candidato
from Resultado.boletim import boletim_da_urna
from Resultado.validar_integridade import relatorio_integridade
from Códigos_fonte.validacoes import gerador_protocolo
import os, random, string, time


def principal():
    os.system('cls')
    print("\n== MENU PRINCIPAL ==")
    print("\n1- Gerenciamento")
    print("2- Votação")
    print("0- Sair")

    i=int(input("\nEscolha a Opção Desejada: "))
    
    if(i==1):
        gerenciamento()
    elif(i==2):
        sistema_votacao()
    elif(i!=0):
        print("A opção escolhida é Inválida\n")
    
    return i
    

def gerenciamento():
    os.system('cls')
    print("\n== GERENCIAMENTO ==")
    print("\n1- Cadastro")
    print("2- Edição")
    print("3- Listar")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))


    if(i==1):
        cadastro()
    elif(i==2):
        edicao()
    elif(i==3):
        listar()

    
    elif(i==0):
        principal()
    return i
    

def cadastro():
    os.system('cls')
    print("\n== CADASTRO ==")
    print("\n0- Voltar")
    print("1- Cadastrar Eleitor")
    print("2- Cadastrar Candidato")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()
    
    elif(i==1):
        cadastrar_eleitor()
        
    elif(i==2):
        cadastrar_candidato()
    
    else:
        print("A opção escolhida é Inválida")
    

def edicao():
    os.system('cls')
    print("\n== EDIÇÃO ==")
    print("\n0- Voltar")
    print("1- Remover Eleitor")
    print("2- Editar Eleitor")
    print("3- Editar Candidato")
    print("4- Buscar Eleitor")
    print("5- Buscar Candidato")
    print("6- Rever Chave de Acesso")
    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()
    elif(i==1):
        remove_titulo = input("Digite o número do título de eleitor do eleitor que deseja remover: ")
        confirmacao = input(f"Tem certeza que deseja remover o eleitor com título {remove_titulo}? (S/N): ")
        
        while confirmacao not in ['S','s','n','N']:
            print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
            confirmacao = input(f"Tem certeza que deseja remover o eleitor com título {remove_titulo}? (S/N): ")
        
        if confirmacao in ['S','s']:
            remover_eleitor(remove_titulo)
        else:
            print("Operação de remoção cancelada. Retornando ao menu de edição...")
            edicao()    
    
    elif(i==2):
        editar_eleitor()
    
    elif(i==3):
        editar_candidato()
    elif(i==4):
        busca()
    elif(i==5):
        buscar_candidato()
    elif(i==6):
        rever_chave_acesso()

    
def listar_eleitores():
    from conexao import conectar
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, titulo, mesario FROM eleitores")
    eleitores = cursor.fetchall()
    cursor.close()
    conexao.close()

    if not eleitores:
        print("Nenhum eleitor cadastrado.")
    else:
        print("\n== LISTA DE ELEITORES ==")
        for e in eleitores:
            print(f"Nome: {e[0]} | Título: {e[1]} | Mesário: {e[2]}")
    
    input("\nPressione Enter para voltar...")
    busca()


def busca():
    os.system('cls')
    print("\n== Busca ==")
    print("\n1- Pesquisar")
    print("2- Listar")
    print("0- Voltar")
    

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        edicao()
    elif(i==1):
        dado=input("Digite o CPF (sem espaços) ou o Título: ")
        resultado = buscar(dado)
        print(resultado)
    elif(i==2):
        listar_eleitores()



def listar():
    os.system('cls')
    print("\n== LISTAR ==")
    print("\n0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()


def sistema_votacao():
    os.system('cls')
    print("\n== SISTEMA DE VOTAÇÃO ==")
    print("\n1- Abertura da Votação")
    print("2- Auditoria")
    print("3- Resultado")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))


    if(i==1):
        abertura_votacao()
    elif(i==2):
        auditoria()
    elif(i==3):
        resultado()
    elif(i==0):
        principal()

    return i



def menu_votacao():
    os.system('cls')  
    print("\n== MENU DE OPERAÇÃO DA URNA ==")
    print("\n1- Votar")
    print("2- Encerrar Votação")
    print("0- Voltar")
        
    i=int(input("\nEscolha a Opção Desejada: "))


    if(i==0):
        sistema_votacao()

    elif(i==1):
        votacao()

    elif(i==2):
        encerramento_votacao()

    return i
    

def votacao():
    os.system('cls')
    print("\n== VOTAÇÃO ==")
    print("\n1- Votar")
    print("2- Encerrar Votação")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))
    if(i==0):
        menu_votacao()
    elif(i==1):
        from Votacao.registrar_voto import registrar_voto
        registrar_voto()
    elif(i==2):
        encerramento_votacao()
    else:
        print("A opção escolhida é Inválida\n")
        menu_votacao()

def encerramento_votacao():
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    digitos = ''.join(random.choices(string.digits, k=5))
    protocolo_original = f"V{letras}2600{digitos}"
    protocolo_cifrado = cifrar(protocolo_original)

    print(f"\nProtocolo de Encerramento: {protocolo_original}")
    print(f"Protocolo cifrado: {protocolo_cifrado}")

    print("\nEncerrando a votação...")
    time.sleep(2)
    print("\nVotação encerrada com sucesso!")
    input("Pressione Enter para retornar ao menu do sistema de votação.")
    sistema_votacao()


def auditoria():
    os.system('cls')
    print("\n== AUDITORIA ==")
    print("\n1- Log de Ocorrência")
    print("2- Protocolo")
    #print("3- Exibir Log")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()
    elif(i==1):
        print("\n== LOG DE OCORRÊNCIA ==")
        from Votacao.log import exibir_logs
        exibir_logs()
        input("\nPressione Enter para voltar...")
        auditoria()
    elif(i==2):
        gerador_protocolo()
        input("\nPressione Enter para voltar...")
        

def resultado():
    os.system('cls')
    print("\n== RESULTADO ==")
    print("\n1- Boletim de Urna")
    print("2- Resultado Final")
    print("3- Votos por partido")
    print("4- Votos por candidato")
    print("5- Estatistica de comparecimento")
    print("6- Validação de integridade")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()
    elif(i==1):
        boletim_da_urna()
    elif(i==2):
        pass

    elif(i==3):
        votos_por_partido()
    elif(i==4):
        votos_por_candidato()
        resultado()
    elif(i==6):
        relatorio_integridade()



def menu_encerrar_sistema():
    os.system('cls')
    from Votacao.encerrar_votacao import executar_encerramento_logica
    
    sucesso = executar_encerramento_logica()
    
    if sucesso:
        print("Sistema finalizado.")
        exit()
    else:
        return
    


<<<<<<< Updated upstream
if __name__ == "__main__":
    while True:
        opcao = principal()
        if opcao == 0:
            menu_encerrar_sistema()
