def verificar_titulo(titulo):
    titulo = str(titulo).strip()  # Remove espaços em branco
    titulo = ''.join(filter(str.isdigit, titulo))  # Remove caracteres não numéricos
    if len(titulo) != 12 and titulo.isdigit():
            return False
   #Separar as partes  
    sequencial = titulo_n[:8]   # 8 primeiros dígitos
    uf_digitos = titulo_n[8:10] # 9º e 10º dígitos (UF)
    dv1 = int(titulo_n[10])     # 11º dígito (1º DV)
    dv2 = int(titulo_n[11])     # 12º dígito (2º DV)

    uf = int(uf_digitos)
    soma1 = 0

    # Pesos para o 1º DV: sequencial × [2,3,4,5,6,7,8,9]
    pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]
    for i in range (8):
        soma1 += int(sequencial[i]) * pesos1[i]

    resto1 = soma1 % 11

    # Regra especial SP (01) e MG (02): resto 0 → DV = 1
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


    # Pesos para o 2º DV: UF × [7,8] + 1º DV × 9
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


