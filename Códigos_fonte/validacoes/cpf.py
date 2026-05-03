def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
 
    soma = 0 
    soma += int (cpf[0]) * 10
    soma += int (cpf[1]) * 9
    soma += int (cpf[2]) * 8
    soma += int (cpf[3]) * 7
    soma += int (cpf[4]) * 6
    soma += int (cpf[5]) * 5
    soma += int (cpf[6]) * 4
    soma += int (cpf[7]) * 3
    soma += int (cpf[8]) * 2
    
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        resultado = 11 - resto
        if resultado == 10:
            digito1 = 0
        else:
            digito1 = resultado

            
    soma = 0
    soma += int (cpf[0]) * 11
    soma += int (cpf[1]) * 10
    soma += int (cpf[2]) * 9
    soma += int (cpf[3]) * 8
    soma += int (cpf[4]) * 7
    soma += int (cpf[5]) * 6
    soma += int (cpf[6]) * 5
    soma += int (cpf[7]) * 4
    soma += int (cpf[8]) * 3
    soma += int (cpf[9]) * 2
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        resultado = 11 - resto
        if resultado == 10:
            digito2 = 0
        else:
            digito2 = resultado
    
    if int(cpf[10]) != digito2:
        return False
    return True
