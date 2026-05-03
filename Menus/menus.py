
from Códigos_fonte.edicao.remover_eleitor import apagar_eleitor_do_banco as remover_eleitor
from Códigos_fonte.edicao.eleitor import editar_eleitor
from Códigos_fonte.edicao.candidato import editar_candidato
from Códigos_fonte.cadastro import cadastrar_candidato
from Códigos_fonte.edicao.rever_chave import rever_chave_acesso
from Códigos_fonte.cadastro import cadastrar_eleitor
from Votacao.Abertura import abertura_votacao
import busca_eleitor as buscar
from Códigos_fonte.edicao.lista import listar_eleitores
import time
import os # para limpar a tela, se necessário
#import random
#add import do menu do banco de dados, quando for criado
#from validacoes import titulo

# ( !!! APENAS COMENTÁRIOS - APAGAR DEPOIS !!! )
# Menus Feitos: Gerenciamento, Votação 
# Submenus Feitos: Cadastro, Edição, Busca, Listar, Sistema de Votação, Auditoria, Resultado
# Até agora a função "voltar" de todos funciona. Só os últimos submenus inacabados tem funções que quebram o programa

 

def principal():
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
        listar_eleitores()

    
    elif(i==0):
        principal()
    return i
    

def cadastro():
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
        print("A opção escolhida é Inválida\n")
    

def edicao():
    print("\n== EDIÇÃO ==")
    print("\n0- Voltar")
    print("1- Remover Eleitor")
    print("2- Editar Eleitor")
    print("3- Editar Candidato")
    print("4- Buscar Eleitor")
    print("5- Rever Chave de Acesso")
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
        rever_chave_acesso()

    


def busca():
    print("\n== Busca ==")
    print("\n1- Pesquisar")
    print("2- Listar")
    print("0- Voltar")
    

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        edicao()
    elif(i==1):
        dado=input("Digite o CPF (sem espaços) ou o Título: ")
        resultado = buscar.buscar_eleitor(dado)
        print(resultado)
    elif(i==2):
        listar_eleitores()



def listar():
    print("\n== LISTAR ==")
    print("\n0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()


def sistema_votacao():
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
    os.system('clear')  # Limpa a tela para melhor visualização
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
    print("\n== VOTAÇÃO ==")
    print("\n1- Votar")
    pass

def encerramento_votacao():
    print("\nEncerrando a votação...")
    time.sleep(2)  
    print("\nVotação encerrada com sucesso!")
    input("Pressione Enter para retornar ao menu do sistema de votação.")
    sistema_votacao()


def auditoria():
    print("\n== AUDITORIA ==")
    print("\n1- Log de Ocorrência")
    print("2- Protocolo")
    print("3- Exibir Log")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()


def resultado():
    print("\n== RESULTADO ==")
    print("\n1- Boletim de Urna")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()

if __name__ == "__main__":
    principal()
