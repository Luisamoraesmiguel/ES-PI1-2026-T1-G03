CHAVE = [[3, 3], [2, 5]]

def _digito_para_letra(c):
    """ 
    Converte um dígito numérico em letra correspondente para uso na Cifra de Hill (0=A, 1=B, ..., 9=J). 
    
    Args: 
        c (str): Caractere que será convertido. 
        
    Returns: 
        str: Letra correspondente ao dígito ou o próprio caractere caso já seja uma letra. 
    """

    if c.isdigit():
        return chr(ord('A') + int(c))
    return c

def _letra_para_digito(c, era_digito):
    """ 
    Converte uma letra novamente em dígito, caso o caractere original tenha sido numérico. 
    
    Args: 
        c (str): Letra a ser convertida. era_digito (bool): Indica se o caractere original era um dígito. 
        
    Returns: 
        str: Dígito correspondente ou a própria letra. 
    """

    if era_digito:
        return str(ord(c) - ord('A'))
    return c

def _letra_para_num(c):
    """ 
    Converte uma letra em número de acordo com a tabela utilizada na Cifra de Hill (A=1 e Z=0). 
    
    Args: 
        c (str): Letra a ser convertida. 
        
    Returns: 
        int: Valor numérico correspondente à letra. 
    """
    c = c.upper()
    if c == 'Z':
        return 0
    return ord(c) - ord('A') + 1

def _num_para_letra(n):
    """ 
    Converte um número em letra de acordo com a tabela utilizada na Cifra de Hill. 
    
    Args: 
        n (int): Número a ser convertido. 
        
    Returns: 
        str: Letra correspondente ao valor numérico. 
    """
    n = n % 26
    if n == 0:
        return 'Z'
    return chr(ord('A') + n - 1)

def cifrar(texto):
    """ 
    Criptografa um texto utilizando a Cifra de Hill. 
    
    Args: 
        texto (str): Texto original que será criptografado, como CPF, chave ou protocolo. 
        
    Returns: 
        str: Texto criptografado pronto para armazenamento ou utilização no sistema. 
    """
    texto = texto.upper()

    convertido = [_digito_para_letra(c) for c in texto]
    era_digito = [c.isdigit() for c in texto]

    letras = [c for c in convertido if c.isalpha()]
    flags = [era_digito[i] for i, c in enumerate(convertido) if c.isalpha()]

    if len(letras) % 2 != 0:
        letras.append('X')
        flags.append(False)

    resultado = []
    for i in range(0, len(letras), 2):
        n1 = _letra_para_num(letras[i])
        n2 = _letra_para_num(letras[i+1])
        c1 = (CHAVE[0][0] * n1 + CHAVE[0][1] * n2) % 26
        c2 = (CHAVE[1][0] * n1 + CHAVE[1][1] * n2) % 26
        resultado.append(_num_para_letra(c1))
        resultado.append(_num_para_letra(c2))

    return "".join(resultado)

def decifrar(texto_cifrado):
    """ 
    Descriptografa um texto previamente cifrado utilizando a Cifra de Hill. 
   
    Args: 
        texto_cifrado (str): Texto criptografado armazenado no sistema ou banco de dados. 
        
     Returns: 
        str:Texto original descriptografado. 
    """
    
    CHAVE_INV = [
        [(3 * 5) % 26,  (3 * -3) % 26],
        [(3 * -2) % 26, (3 *  3) % 26]
    ]

    texto_cifrado = texto_cifrado.upper()
    letras = [c for c in texto_cifrado if c.isalpha()]

    resultado = []
    for i in range(0, len(letras), 2):
        n1 = _letra_para_num(letras[i])
        n2 = _letra_para_num(letras[i+1])
        p1 = (CHAVE_INV[0][0] * n1 + CHAVE_INV[0][1] * n2) % 26
        p2 = (CHAVE_INV[1][0] * n1 + CHAVE_INV[1][1] * n2) % 26
        resultado.append(_num_para_letra(p1))
        resultado.append(_num_para_letra(p2))

    return "".join(resultado)