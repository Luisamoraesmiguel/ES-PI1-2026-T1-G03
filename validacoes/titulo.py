def validar_titulo_eleitor(titulo_n):
    """
    Realiza a validação do formato do título de eleitor.
    
    Args:
        titulo_n (str/int): O número do título a ser validado.
        
    Returns:
        int: Retorna 1 se o título tiver 12 dígitos numéricos, 0 caso contrário.
    """
    try:
        # Converte para string e limpa espaços extras
        titulo_limpo = str(titulo_n).strip()
        
        # Verifica se tem exatamente 12 caracteres e se todos são dígitos
        if len(titulo_limpo) == 12 and titulo_limpo.isdigit():
            return 1
        else:
            return 0
            
    except Exception as e:
        print(f"Erro inesperado na validação: {e}")
        return 0