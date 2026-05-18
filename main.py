from Menus import menus

i=None

while(i!=0):
    i=int(menus.principal())

    if(i==1):
        menus.gerenciamento()
    elif(i==2):
        menus.votacao()
    elif(i!=0):
        print("A opção escolhida é Inválida\n")
        

        
