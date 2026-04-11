import menus

# ( !!! APENAS COMENTÁRIOS - APAGAR DEPOIS !!! )
# O programa começa aqui com um loop. Depois da opção escohida a lógica acontece toda em menus.py (não sei se é a melhor ideia)
# A parte dos menus foi feita até certo ponto - É preciso terminar os submenus e as funções deles
# ARRUMAR - QUANDO SE AVANÇA MUITOS MENUS E CLICO PARA VOLTAR ATÉ O MENU PRINCIPAL. DAÍ NELE É PRECISO DIGITAR A OPÇÃO ESCOLHIDA DUAS VEZES PARA DAR CERTO



# Programa Principal
i=None

while(i!=0):
    i=int(menus.principal())

    if(i==1):
        menus.gerenciamento()
    elif(i==2):
        menus.votacao()
    elif(i!=0):
        print("A opção escolhida é Inválida\n")
        

        
