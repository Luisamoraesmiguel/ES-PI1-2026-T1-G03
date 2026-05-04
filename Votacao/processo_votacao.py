import os
import time
from busca_eleitor import busca_eleitor
from Códigos_fonte.validacoes import mesario
from Votacao import registrar_voto

def realizar_fluxo_votacao():

    print("\n" + "="*30)
    print("      URNA ELETRÔNICA")
    print("="*30)

    t = input("Título de Eleitor: ")
    c4 = input("4 primeiros dígitos do CPF: ")
    ch = input("Chave de Acesso: ").upper().strip()

    eleitor = mesario.validar_identidade_eleitor(t, c4, ch)

    if eleitor == "INVALIDO":
        print("\n[ERRO] Credenciais incorretas.")
    elif eleitor == "JA_VOTOU":
        print("\n[ERRO] Este eleitor já realizou o voto anteriormente.")
    elif eleitor == "CPF_ERRADO":
        print("\n[ERRO] CPF não confere.")
    else:
        # Eleitor validado com sucesso!
        processar_escolha_candidato(t, eleitor['nome'])


def processar_escolha_candidato(titulo_eleitor, nome_eleitor):
   
    voto_finalizado = False
    
    print(f"\nBem-vindo(a), {nome_eleitor}!")

    while voto_finalizado == False:
        numero = input("\nDigite o número do candidato: ")
        candidato = busca_eleitor(numero)

        if candidato:
            print(f"CANDIDATO: {candidato['nome']} | PARTIDO: {candidato['partido']}")
        else:
            print("CANDIDATO NÃO ENCONTRADO - VOTO SERÁ NULO.")
            numero = "00"

        # RF002.01.06.06: Opção de confirmar ou não
        confirmar = input("Confirma o voto? (S/N): ").upper().strip()
        
        if confirmar == "S":
            # RF002.01.06.07, 08 e 09: Grava e mostra protocolo
            protocolo = registrar_voto.gravar_voto_no_banco(numero, titulo_eleitor)
            
            print("\n" + "*"*40)
            print("          VOTO CONFIRMADO!")
            print(f"  PROTOCOLO: {protocolo}")
            print("*"*40)
            input("\nPressione Enter para concluir...")
            
            voto_finalizado = True # Encerra o loop do candidato
        else:
            print("\nVoltando para a inserção do número...")
            # O loop continuará pois voto_finalizado ainda é False

