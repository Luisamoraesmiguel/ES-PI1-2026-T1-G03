from Códigos_fonte.edicao.remover_eleitor import apagar_eleitor_do_banco as remover_eleitor
from Códigos_fonte.edicao.eleitor import editar_eleitor
from Códigos_fonte.edicao.candidato import editar_candidato
from Códigos_fonte.edicao.rever_chave import rever_chave_acesso
from Códigos_fonte.edicao.busca_eleitor import buscar_eleitor as buscar, buscar_candidato
from Códigos_fonte.edicao.lista import listar_eleitores, listar_candidatos
from Códigos_fonte.cadastro import cadastrar_candidato, cadastrar_eleitor
from Códigos_fonte.validacoes.cpf import validar_cpf
from Votacao.Abertura import abertura_votacao
from Criptografia import cifrar
from Resultado.vts_partido import votos_por_partido
from Resultado.vts_candidato import votos_por_candidato
from Resultado.comparecimento import estatistica_comparecimento
from Resultado.boletim import boletim_da_urna
import os, random, string
from Códigos_fonte.validacoes.titulo import verificar_titulo
from Votacao.processo_votacao import realizar_fluxo_votacao
from Códigos_fonte.validacoes.mesario import verificar_mesario
from Resultado.resultado_final import resultado_final
from Resultado.validar_integridade import relatorio_integridade

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
        gerenciamento()

    elif(i==2):
        cadastrar_candidato()
        gerenciamento()

    else:
        print("A opção escolhida é Inválida\n")
    

def edicao():
    os.system('cls')
    print("\n== EDIÇÃO ==")
    print("\n0- Voltar")
    print("1- Remover Eleitor")
    print('2- Remover Candidato') 
    print("3- Editar Eleitor")
    print("4- Editar Candidato")
    print("5- Buscar")
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
        remove_numero = input("Digite o número do candidato que deseja remover: ")
        confirmacao = input(f"Tem certeza que deseja remover o candidato com número {remove_numero}? (S/N): ")
        
        while confirmacao not in ['S','s','n','N']:
            print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
            confirmacao = input(f"Tem certeza que deseja remover o candidato com número {remove_numero}? (S/N): ")
        
        if confirmacao in ['S','s']:
            from Códigos_fonte.edicao.remover_eleitor import apagar_candidato_do_banco as remover_candidato
            remover_candidato(remove_numero)
        else:
            print("Operação de remoção cancelada. Retornando ao menu de edição...")
            edicao()
    
    elif(i==3):
        editar_eleitor()
    
    elif(i==4):
        editar_candidato()

    elif(i==5):
        busca()

    elif(i==6):
        rever_chave_acesso()

    


def busca():
    os.system('cls')
    print("\n== Busca ==")
    print("\n1- Pesquisar eleitor")
    print("2- Pesquisar candidato")
    print("0- Voltar")
    

    i=int(input("Escolha a Opção Desejada: "))

    if(i==0):
        edicao()

    elif(i==1):
        dado=input("Digite o CPF (sem espaços) ou o Título: ")
        resultado = buscar(dado)
        

    elif(i==2):
        dado=input("Digite o número do candidato: ")
        resultado = buscar_candidato(dado)
        

    elif(i==4):
        buscar_candidato()




def listar():
    os.system('cls')
    print("\n== LISTAR ==")
    print("\n1- Listar Eleitores")
    print("2- Listar Candidatos")
    print("\n0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))

    if(i==0):
        gerenciamento()

    elif(i==1):
        listar_eleitores()

    elif(i==2):
        listar_candidatos()

    else:
        print("A opção escolhida é Inválida\n")
        listar()


def sistema_votacao():
    os.system('cls')
    print("\n== SISTEMA DE VOTAÇÃO ==")
    print("\n1- Abertura da Votação")
    print("2- Auditoria")
    print("3- Resultado")
    print("0- Voltar")

    i=int(input("\nEscolha a Opção Desejada: "))


    if(i==1):
        if not abertura_votacao():
            return sistema_votacao()
             
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
        realizar_fluxo_votacao()

    elif(i==2):
        encerramento_votacao()

    return i
    

def encerramento_votacao():
    print("\n" + "="*30)
    print(" ENCERRAMENTO DE VOTAÇÃO")
    print("="*30)
    
    status = "pendente"
    
    while status == "pendente":
        nome = input("\nDigite o nome completo do mesário: ").upper().strip()
        titulo = input("Digite o número do título de eleitor do mesário: ").strip()
        cpf_4 = input("Digite os 4 primeiros dígitos do CPF do mesário: ").strip()
        chave = input("Digite a chave de acesso do mesário: ").strip()

        resultado = verificar_mesario(titulo, cpf_4, chave)

        if isinstance(resultado, dict):
            print(f"\n[OK] Mesário {resultado['nome']} identificado.")
            escolha = input("\nDeseja realmente encerrar a votação? (S/N): ").upper().strip()
            
            if escolha == 'S':
                segunda_chave = input("Confirme sua chave de acesso para lacrar a urna: ").strip()
                if segunda_chave == chave:
                    print("\n" + "*"*40)
                    print(">>> VOTAÇÃO ENCERRADA COM SUCESSO! <<<")
                    print("*"*40)
                    status = "concluido"
                else:
                    print("\n[ERRO] A confirmação da chave falhou. Tente novamente.")
                    menu_votacao()
            else:
                print("\nEncerramento cancelado.")
                status = "concluido"
                menu_votacao()
        else:
            print("\n[ERRO] Dados incorretos. Tente novamente.")
            menu_votacao()

    input("\nPressione Enter para retornar ao menu.")
    sistema_votacao()


def auditoria():
    os.system('cls')
    print("\n== AUDITORIA ==")
    print("\n1- Log de Ocorrência")
    print("2- Protocolo")
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
        print("\n== PROTOCOLO DE VOTAÇÃO ==")
        from Auditoria.protocolos import exibir_protocolos
        exibir_protocolos()

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
        resultado_final()
    elif(i==3):
        votos_por_partido()
    elif(i==4):
        votos_por_candidato()
    elif(i==5):
        estatistica_comparecimento()
    elif(i==6):
        relatorio_integridade()
    else:
        print("A opção escolhida é Inválida\n")
        resultado()

    



def menu_encerrar_sistema():
    os.system('cls')
    from Votacao.encerrar_votacao import executar_encerramento_logica
    
    sucesso = executar_encerramento_logica()
    
    if sucesso:
        print("Sistema finalizado.")
        exit()
    else:
        return
    


if __name__ == "__main__": # Início do programa
    principal()

