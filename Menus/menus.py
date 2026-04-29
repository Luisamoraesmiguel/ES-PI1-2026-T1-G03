
from Códigos_fonte.validacoes.cpf import validar_cpf
from Códigos_fonte.validacoes.titulo import verificar_titulo
import Criptografia 
import Códigos_fonte.cadastro as acao_cadastro
from Códigos_fonte.validacoes.mesario import verificar_mesario
from Códigos_fonte.zerezima import zerezima 
from remover_eleitor import apagar_eleitor_do_banco as remover_eleitor

import time
import chave
import os # para limpar a tela, se necessário
#import random
#add import do menu do banco de dados, quando for criado
#from validacoes import titulo

# ( !!! APENAS COMENTÁRIOS - APAGAR DEPOIS !!! )
# Menus Feitos: Gerenciamento, Votação 
# Submenus Feitos: Cadastro, Edição, Busca, Listar, Sistema de Votação, Auditoria, Resultado
# Até agora a função "voltar" de todos funciona. Só os últimos submenus inacabados tem funções que quebram o programa

 

#lista de menus

def principal():
    print("\n== MENU PRINCIPAL ==")
    print("1- Gerenciamento")
    print("2- Votação")
    print("0- Sair")

    i=int(input("Escolha a Opção Desejada: "))
    
    if(i==1):
        gerenciamento()
    elif(i==2):
        sistema_votacao()
    elif(i!=0):
        print("A opção escolhida é Inválida\n")
    
    return i
    
 #====================================================   


#======== GERENCIAMENTO ============================

def gerenciamento():
    print("\n== GERENCIAMENTO ==")
    print("1- Cadastro")
    print("2- Edição")
    print("3- Busca")
    print("4- Listar")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))


    if(i==1):
        cadastro()
    elif(i==2):
        edicao()
    elif(i==3):
        busca()
    elif(i==4):
        listar()
    
    elif(i==0):
        principal()
    return i
    

def cadastro():
    print("\n== CADASTRO ==")
    print("0- Voltar")
    print("1- Cadastrar Eleitor")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()
    
    elif(i==1):
        nome = input("Digite o nome completo do eleitor: ").upper().strip()  # Converte para maiúsculas e remove espaços extras 
        titulo = ""
        cpf = ""
        votou = 'N'
        mesario = input("O eleitor é mesário? (S/N): ").upper().strip()  # Converte para maiúsculas e remove espaços extras
        #while mesario not in ['S', 'N']:
            #print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
            #mesario = input("O eleitor é mesário? (S/N): ")
        while not validar_cpf(cpf):
            cpf = input("Digite o CPF do eleitor (apenas números): ")
            if not validar_cpf(cpf):
                print("CPF inválido. Por favor, tente novamente.")

        titulo_valido = False # Inicializa a variável de controle para o loop de validação do título
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
        print('Senha: ',senha)

        cpf_cifrado = Criptografia.cifrar(cpf)
        sucesso = acao_cadastro.cadastrar_eleitor(nome, cpf_cifrado, titulo, mesario, votou, senha)

        if sucesso == 1:
            print("\nEleitor cadastrado e criptografado com sucesso!")
        else:
            print("\nErro ao salvar no banco de dados.")
    
    else:
        print("A opção escolhida é Inválida\n")
    

def edicao():
    print("\n== EDIÇÃO ==")
    print("0- Voltar")
    print("1- Remover Eleitor")

    i=int(input("Escolha a Opção Desejada: "))

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



def busca():
    print("\n== Busca ==")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()

def listar():
    print("\n== LISTAR ==")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()

#====================================================
  


#======== SISTEMA DE VOTAÇÃO ============================

def sistema_votacao():
    print("\n== SISTEMA DE VOTAÇÃO ==")
    print("1- Abertura da Votação")
    print("2- Auditoria")
    print("3- Resultado")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))


    if(i==1):
        abertura_votacao()
    elif(i==2):
        auditoria()
    elif(i==3):
        resultado()
    elif(i==0):
        principal()

    return i


#=== ABERTURA DA VOTAÇÃO ===
def abertura_votacao():
        os.system('clear')  # Limpa a tela para melhor visualização
        print("\n== ABERTURA DO SISTEMA DE VOTAÇÃO ==")

        #Validação do mesário
        print("\n IDENTIFICAÇÃO DO MESÁRIO")
        titulo= input("Digite o número do título de eleitor do mesário: ")
        cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
        chave = input("Digite a chave de acesso do mesário: ").upper().strip()  # Converte para maiúsculas e remove espaços extras
        
        while not verificar_mesario(titulo, cpf, chave):
            print("Mesário não identificado. Por favor, tente novamente.")
            N=input("Deseja tentar novamente? (S/N): ")
            if N == 'N' or N == 'n':
                print("Retornando ao menu do sistema de votação...")
                sistema_votacao()
            titulo= input("Digite o número do título de eleitor do mesário: ")
            cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
            chave = input("Digite a chave de acesso do mesário: ").upper().strip()  # Converte para maiúsculas e remove espaços extras


        print("Mesário identificado com sucesso!")
        input("Pressione Enter para realizar a Zerezima")

        while not zerezima():
                print("Erro ao realizar a Zerezima. Por favor, tente novamente.")
                input("Pressione Enter para realizar a Zerezima")
        print("Zerezima realizada com sucesso!")

        votacao= input("Deseja continuar o processo de votação? (S/N): ")
        if votacao == 'S' or votacao == 's':
            menu_votacao()

        elif votacao == 'N' or votacao == 'n':
            print("retornando para menu do sistema de votação...")
            sistema_votacao()

        while votacao != 'S' and votacao != 'N' and votacao != 's' and votacao != 'n':
            print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
            votacao = input("Deseja continuar o processo de votação? (S/N): ")

            
def menu_votacao():
    os.system('clear')  # Limpa a tela para melhor visualização
    print("\n== MENU DE OPERAÇÃO DA URNA ==")
    print("1- Votar")
    print("2- Encerrar Votação")
    print("0- Voltar")
        
    i=int(input("Escolha a Opção Desejada: "))


    if(i==0):
        sistema_votacao()

    elif(i==1):
        votacao()

    elif(i==2):
        encerramento_votacao()

    return i
    

#== VOTACAO == 
def votacao():
    print("\n== VOTAÇÃO ==")
    print("1- Votar")
    pass

#== ENCERRAMENTO DA VOTAÇÃO ===
def encerramento_votacao():
    print("\nEncerrando a votação...")
    time.sleep(2)  # Simula o processo de encerramento
    print("Votação encerrada com sucesso!")
    input("Pressione Enter para retornar ao menu do sistema de votação.")
    sistema_votacao()


#== AUDITORIA ===
def auditoria():
    print("\n== AUDITORIA ==")
    print("1- Log de Ocorrência")
    print("2- Protocolo")
    print("3- Exibir Log")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()


#== RESULTADO ===
def resultado():
    print("\n== RESULTADO ==")
    print("1- Boletim de Urna")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        sistema_votacao()

if __name__ == "__main__":
    principal()
