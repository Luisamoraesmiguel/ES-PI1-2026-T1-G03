def verificar_titulo(titulo):
    titulo = str(titulo).strip()  
    titulo = ''.join(filter(str.isdigit, titulo))  
    if len(titulo) != 12 or not titulo.isdigit():
            return False
   
    sequencial = titulo[:8]   
    uf_digitos = titulo[8:10] 
    dv1 = int(titulo[10])     
    dv2 = int(titulo[11])     

    uf = int(uf_digitos)
    soma1 = 0

    pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]
    for i in range (8):
        soma1 += int(sequencial[i]) * pesos1[i]

    resto1 = soma1 % 11

    if resto1 == 10:
        primeiro_dv = 0

    elif resto1 == 0:
        if uf in (1, 2):
            primeiro_dv = 1
        else:
            primeiro_dv = 0

    else:
        primeiro_dv = resto1
        
    if dv1 != primeiro_dv:
        return False


    soma2 = (int(uf_digitos[0]) * 7) + (int(uf_digitos[1]) * 8) + (primeiro_dv * 9)
    resto2 = soma2 % 11

    if resto2 == 10:
        segundo_dv = 0
    elif resto2 == 0:
        if uf in (1, 2):
            segundo_dv = 1
        else:
            segundo_dv = 0
    else:
        segundo_dv = resto2

    return segundo_dv == dv2


