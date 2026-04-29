# Criptografia
import numpy as np

CHAVE = np.array([[3, 3], [2, 5]])


def cifrar(texto):
    """Criptografa um texto usando a Cifra de Hill com duplicação de caractere ímpar.
    
    Args:
        texto (str): O dado original (CPF, Chave ou Protocolo).
        
    Returns:
        str: O texto cifrado pronto para o banco de dados."""
    
    numeros = [ord(c) for c in texto]
    
    if len(numeros) % 2 != 0:
        numeros.append(numeros[-1]) 
        
    resultado = []
    
    for i in range(0, len(numeros), 2):
        bloco = np.array([numeros[i], numeros[i+1]])
        
    
        cifrado = np.dot(CHAVE, bloco) % 256 
        
        resultado.append(int(cifrado[0]))
        resultado.append(int(cifrado[1]))
        
    return "".join(chr(n) for n in resultado)
#para testar, apagar depois!!!!
#cpf=str(input("Digite o CPF: "))
#resultado = cifrar(cpf)
#print("Lista de números gerados:", [ord(c) for c in resultado])
#print("Tamanho total:", len(resultado))

def decifrar(texto_cifrado):
    numeros = [ord(c) for c in texto_cifrado]
    resultado = []

    # Inversa correta da matriz [[3,3],[2,5]] mod 256
    # det = 3*5 - 3*2 = 9, e 9 * 57 mod 256 = 1, então det_inv = 57
    det_inv = 57
    CHAVE_INVERSA = [
        [det_inv * 5  % 256, det_inv * (-3) % 256],
        [det_inv * (-2) % 256, det_inv * 3  % 256]
    ]

    for i in range(0, len(numeros), 2):
        a = numeros[i]
        b = numeros[i+1]
        x = (CHAVE_INVERSA[0][0] * a + CHAVE_INVERSA[0][1] * b) % 256
        y = (CHAVE_INVERSA[1][0] * a + CHAVE_INVERSA[1][1] * b) % 256
        resultado.append(x)
        resultado.append(y)

    return "".join(chr(n) for n in resultado)