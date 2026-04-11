
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


def cadastro():
    print("\n== CADASTRO ==")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()

def edicao():
    print("\n== EDIÇÃO ==")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()

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
  


#======== VOTAÇÃO ============================

def votacao():
    print("\n== VOTAÇÃO ==")
    print("1- Sistema de Votação")
    print("2- Auditoria")
    print("3- Resultado")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==1):
        sistemaVotacao()
    elif(i==2):
        auditoria()
    elif(i==3):
        resultado()
    elif(i==0):
        principal()


#=== SISTEMA DE VOTAÇÃO ===
def sistemaVotacao():
    print("\n== SISTEMA DE VOTAÇÃO ==")
    print("1- Votar")
    print("2- Encerrar Votação")
    print("3- Validar Mesário")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        votacao()


#== AUDITORIA ===
def auditoria():
    print("\n== AUDITORIA ==")
    print("1- Log de Ocorrência")
    print("2- Protocolo")
    print("3- Exibir Log")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        votacao()


#== RESULTADO ===
def resultado():
    print("\n== RESULTADO ==")
    print("1- Boletim de Urna")
    print("0- Voltar")

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        votacao()