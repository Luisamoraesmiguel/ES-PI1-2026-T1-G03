import os
from Códigos_fonte.edicao.busca_eleitor import buscar_candidato as busca
from Códigos_fonte.validacoes import eleitor_validacao
from Votacao import registrar_voto
from Votacao.log import registrar_log

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def realizar_fluxo_votacao():

    limpar_tela()
    print("\n" + "="*30)
    print("      URNA ELETRÔNICA")
    print("="*30)

    t = input("Título de Eleitor: ")
    c4 = input("4 primeiros dígitos do CPF: ")
    ch = input("Chave de Acesso: ").upper().strip() 

    eleitor = eleitor_validacao.verificar_eleitor(t, c4, ch)

    if eleitor == "INVALIDO":
        print("\n[ERRO] Credenciais incorretas.")
        registrar_log("ALERTA: Tentativa de acesso negado - credenciais invalidas")
        from Menus.menus import menu_votacao
        menu_votacao()
    
    elif eleitor == "JA_VOTOU":
        print("\n[ERRO] Este eleitor já realizou o voto anteriormente.")
        registrar_log("ALERTA: Tentativa de voto duplo")
        from Menus.menus import menu_votacao
        menu_votacao()

    elif eleitor == "CPF_ERRADO":
        print("\n[ERRO] CPF não confere.")
        registrar_log("ALERTA: Tentativa de voto com CPF incorreto")
        from Menus.menus import menu_votacao
        menu_votacao()

    else:
        
        processar_escolha_candidato(t, eleitor[0])
        registrar_log("SUCESSO: Voto realizado com sucesso.")
        return


def processar_escolha_candidato(titulo_eleitor, nome_eleitor):
   
    voto_finalizado = False
    
    print(f"\nBem-vindo(a), {nome_eleitor}!")

    while voto_finalizado == False:
        numero = input("\nDigite o número do candidato: ")
        candidato = busca(numero)

        if candidato:
            print(f"CANDIDATO: {candidato['nome']} | Numero: {candidato['numero']} | PARTIDO: {candidato['partido']}")
        else:
            print("CANDIDATO NÃO ENCONTRADO - VOTO SERÁ NULO.")
            numero = "00"
        confirmar = input("Confirma o voto? (S/N): ").upper().strip()
        
        if confirmar == "S":
            
            protocolo = registrar_voto.gravar_voto_no_banco(candidato['id'], titulo_eleitor)
            
            print("\n" + "*"*40)
            print("          VOTO CONFIRMADO!")
            print(f"  PROTOCOLO: {protocolo}".center(40))
            print("*"*40)
            input("\nPressione Enter para concluir...")
            
            voto_finalizado = True 
            from Menus.menus import menu_votacao
            menu_votacao()
            return
        else:
            print("\nVoltando para a inserção do número...")

           

