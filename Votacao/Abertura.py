import os
from Códigos_fonte.validacoes.mesario import verificar_mesario
from Códigos_fonte.zerezima import zerezima
from Votacao.log import registrar_log
from Menus.menus import menu_votacao

def abertura_votacao():

    """
    Inicia o processo de abertura da votação, identificando o mesário e executando a zerezima.

    Args:
        Nenhum.

    Returns:
        bool: Retorna True se a abertura e a zerezima forem bem-sucedidas, False caso contrário.
    """

    os.system('cls')
    print("\n== ABERTURA DO SISTEMA DE VOTAÇÃO ==")

    print("\n IDENTIFICAÇÃO DO MESÁRIO")
    titulo = input("\nDigite o número do título de eleitor do mesário: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
    chave = input("Digite a chave de acesso do mesário: ").upper().strip()

    while verificar_mesario(titulo, cpf, chave) == "INVALIDO":
        print("Mesário não identificado. Por favor, tente novamente.")
        registrar_log("ALERTA: Tentativa de acesso negado")
        N = input("Deseja tentar novamente? (S/N): ").upper().strip()
        if N == 'N':
            print("Retornando ao menu do sistema de votação...")
            return False
        titulo = input("\nDigite o número do título de eleitor do mesário: ")
        cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
        chave = input("Digite a chave de acesso do mesário: ").upper().strip()

    print("\nMesário identificado com sucesso!")
    
    input("Pressione Enter para realizar a Zerezima")

    while not zerezima():
        print("\nErro ao realizar a Zerezima. Por favor, tente novamente.")
        input("Pressione Enter para realizar a Zerezima")

    registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")

    print("\nZerezima realizada com sucesso!")
    
    # Chama o menu e encerra a função
    menu_votacao()
    return True