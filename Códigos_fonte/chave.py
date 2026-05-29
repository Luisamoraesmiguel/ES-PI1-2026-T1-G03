import random
import Criptografia

def gerar_chave(nome_completo):

    """
    Gera uma chave de acesso única para o eleitor com base no
    nome completo. Usa as duas primeiras letras do primeiro nome,
    a inicial do segundo nome e quatro dígitos aleatórios.

    Args:
        nome_completo (str): Nome completo do eleitor em qualquer capitalização.

    Returns:
        str: Chave de acesso em texto claro no formato XXX9999
             (ex: JOS1234).
    """

    partes_nome = nome_completo.strip().upper().split()

    if len(partes_nome) < 1:
        return "Nome Inválido"
    
    primeiro_nome = partes_nome[0]

    if len(partes_nome) > 1:
        segundo_nome = partes_nome[1]
    else:
        segundo_nome = 'X'

    prefixo = primeiro_nome[:2] + segundo_nome[0]

    digitos = str(random.randint(1000, 9999))

    chave_original = f"{prefixo}{digitos}"
    chave_cifrada = Criptografia.cifrar(chave_original)

    return chave_original



    
