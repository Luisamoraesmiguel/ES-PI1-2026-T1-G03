CHAVE = [[3, 3], [2, 5]]

def _digito_para_letra(c):
    """Converte dígito numérico para letra (0=A, 1=B, ..., 9=J).
    Args:
        c (str): Caractere a ser convertido.
    Returns:
        str: Letra correspondente ou o próprio caractere se já for letra.
    """
    if c.isdigit():
        return chr(ord('A') + int(c))
    return c

def _letra_para_digito(c, era_digito):
    """Converte letra de volta para dígito se necessário.
    Args:
        c (str): Letra a ser convertida.
        era_digito (bool): Se o caractere original era um dígito.
    Returns:
        str: Dígito correspondente ou a própria letra.
    """
    if era_digito:
        return str(ord(c) - ord('A'))
    return c

def _letra_para_num(c):
    """Converte letra para número conforme tabela da Cifra de Hill (A=1, Z=0).
    Args:
        c (str): Caractere a ser convertido.
    Returns:
        int: Número correspondente.
    """
    c = c.upper()
    if c == 'Z':
        return 0
    return ord(c) - ord('A') + 1

def _num_para_letra(n):
    """Converte número para letra conforme tabela da Cifra de Hill.
    Args:
        n (int): Número a ser convertido.
    Returns:
        str: Letra correspondente.
    """
    n = n % 26
    if n == 0:
        return 'Z'
    return chr(ord('A') + n - 1)

def cifrar(texto):
    """Criptografa um texto usando a Cifra de Hill.
    Args:
        texto (str): O dado original (CPF, Chave ou Protocolo).
    Returns:
        str: O texto cifrado pronto para o banco de dados.
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
    """Descriptografa um texto cifrado pela Cifra de Hill.
    Args:
        texto_cifrado (str): O texto cifrado armazenado no banco.
    Returns:
        str: O texto original descriptografado.
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