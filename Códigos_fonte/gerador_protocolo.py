import random
import string

def criar_novo_protocolo(numero_candidato):
    
    """
    Gera um protocolo de votação seguindo o padrão oficial do LAD.Py.
    Padrão: V + 2 letras + 26 + Candidato (2 dígitos) + 5 números.

    Args:
        numero_candidato (str ou int): O número do candidato escolhido.

    Returns:
        str: O protocolo em texto claro para ser exibido ao eleitor.
    """
     
     prefixo = "V"

     
     letras = ''.join(random.choices(string.ascii_uppercase, k=2))

     ano = 26

     cand = str(numero_candidato).zfill(2)  

     digitos = ''.join(random.choices(string.digits, k=5))

     protocolo_final = f"{prefixo}{letras}{ano}{cand}{digitos}"

     return protocolo_final
