import random
import Criptografia

def gerar_chave(nome_completo):

    #.strip() - Remove todos espaços
    #.upper() - Deixa todas letras em maiúsculo
    #.split() - Divide o nome em uma lista
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



    