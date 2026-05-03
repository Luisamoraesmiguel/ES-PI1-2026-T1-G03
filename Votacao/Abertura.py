import os
from Códigos_fonte.validacoes.mesario import verificar_mesario
from Códigos_fonte.zerezima import zerezima

def abertura_votacao():
    os.system('clear')
    print("\n== ABERTURA DO SISTEMA DE VOTAÇÃO ==")

    print("\n IDENTIFICAÇÃO DO MESÁRIO")
    titulo = input("\nDigite o número do título de eleitor do mesário: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
    chave = input("Digite a chave de acesso do mesário: ").upper().strip()

    while not verificar_mesario(titulo, cpf, chave):
        print("Mesário não identificado. Por favor, tente novamente.")
        N = input("Deseja tentar novamente? (S/N): ")
        if N == 'N' or N == 'n':
            print("Retornando ao menu do sistema de votação...")
            return
        titulo = input("\nDigite o número do título de eleitor do mesário: ")
        cpf = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
        chave = input("Digite a chave de acesso do mesário: ").upper().strip()

    print("\nMesário identificado com sucesso!")
    input("Pressione Enter para realizar a Zerezima")

    while not zerezima():
        print("\nErro ao realizar a Zerezima. Por favor, tente novamente.")
        input("Pressione Enter para realizar a Zerezima")
    print("\nZerezima realizada com sucesso!")
