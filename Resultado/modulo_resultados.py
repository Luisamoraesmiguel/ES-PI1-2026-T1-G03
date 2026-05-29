from conexao import conectar

def exibir_boletim_urna_completo():
    """ 
    Exibe o boletim de urna completo, listando os votos por candidato em ordem alfabética e apresentando o vencedor da eleição. 
    
    Args: 
        Nenhum. 
        
    Returns: 
        None: Não retorna valores. Apenas exibe as informações do boletim de urna no terminal. 
    """
    
    print("\n" + "="*60)
    print("BOLETIM DE URNA")
    print("="*60)
    conexao = conectar()
    cursor = conexao.cursor()
    

    cursor.execute("SELECT * FROM votos")
    votos = cursor.fetchall()
    
    
    try:
        cursor.execute("SELECT numero_candidato, nome_candidato, partido_candidato FROM candidatos ORDER BY nome_candidato ASC")
        lista_candidatos = cursor.fetchall()
    except:
        
        lista_candidatos = [("99", "Candidato Nulo/Geral", "PARTIDO")]

    if not votos:
        print("Nenhum voto registrado na urna por enquanto.")
    else:
        
        contagem = {}
        for linha in votos:
            voto_candidato = str(linha[1]) if len(linha) > 1 else str(linha[0])
            contagem[voto_candidato] = contagem.get(voto_candidato, 0) + 1
            
        print(f"{'CANDIDATO':<25} | {'Nº':<6} | {'PARTIDO':<10} | TOTAL VOTOS")
        print("-"*60)
        
        vencedor_num = None
        vencedor_nome = "Nenhum"
        vencedor_partido = "Nenhum"
        max_votos = -1
        
        for cand_num, cand_nome, cand_part in lista_candidatos:
            total_cand_votos = contagem.get(str(cand_num), 0)
            print(f"{cand_nome:<25} | {cand_num:<6} | {cand_part:<10} | {total_cand_votos} voto(s)")
            
            if total_cand_votos > max_votos:
                max_votos = total_cand_votos
                vencedor_num = cand_num
                vencedor_nome = cand_nome
                vencedor_partido = cand_part
                
        print("-" * 60)
        print("💥 RESULTADO DA ELEIÇÃO (VENCEDOR):")
        print(f"Nome: {vencedor_nome} | Nº: {vencedor_num} | Partido: {vencedor_partido}")
        print(f"Total de Votos Obtidos: {max_votos}")
        
    cursor.close()
    conexao.close()
    print("="*60)

def mostrar_comparecimento():
    """ 
    Exibe a estatística de comparecimento eleitoral, apresentando a quantidade absoluta de eleitores que votaram e o percentual de participação. 
    
    Args: 
        Nenhum. 
        
    Returns: 
        None: Não retorna valores. Apenas exibe os dados estatísticos no terminal. 
    """

    print("\n" + "="*60)
    print("ESTATÍSTICA DE COMPARECIMENTO")
    print("="*60)
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total = cursor.fetchone()[0]
    
    try:
        cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 'Já Votou'")
        votos = cursor.fetchone()[0]
    except:
        votos = 0
    
    if total == 0:
        print("Nenhum eleitor cadastrado no sistema.")
    else:
        percentual = (votos / total) * 100
        print(f"Quantidade absoluta de pessoas que votaram: {votos}")
        print(f"Total de eleitores aptos: {total}")
        print(f"Percentual de participação: {percentual:.2f}%")
        
    cursor.close()
    conexao.close()
    print("="*60)

def mostrar_partidos():
    """ 
    Exibe a quantidade total de votos agrupados por partido político ou legenda cadastrada. 
    
    Args: 
        Nenhum. 
    
    Returns: 
        None: Não retorna valores. Apenas apresenta a contabilização de votos por partido no terminal. 
    """
    print("\n" + "="*60)
    print("VOTOS POR PARTIDO")
    print("="*60)
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM votos")
    votos = cursor.fetchall()
    
    if not votos:
        print("Nenhum voto computado no banco de dados.")
    else:
        contagem_partidos = {}
        try:
            cursor.execute("SELECT numero_candidato, partido_candidato FROM candidatos")
            mapeamento_partidos = dict(cursor.fetchall())
        except:
            mapeamento_partidos = {}

        for linha in votos:
            voto_candidato = linha[1] if len(linha) > 1 else linha[0]
            # Busca o partido do candidato ou joga em nulo
            partido = mapeamento_partidos.get(voto_candidato, "Legenda Nula/Brancos")
            contagem_partidos[partido] = contagem_partidos.get(partido, 0) + 1

        print(f"{'LEGENDA PARTIDÁRIA':<30} | TOTAL DE VOTOS")
        print("-"*50)
        for partido, total_votos in contagem_partidos.items():
            print(f"{partido:<30} | {total_votos} voto(s)")
            
    cursor.close()
    conexao.close()
    print("="*60)

def mostrar_integridade():
    """
    Valida a integridade da eleição comparando a quantidade de votos registrados com a quantidade de eleitores que possuem o status 'Já Votou'. 
    
    Args: 
        Nenhum. 
        
    Returns: 
        None: Não retorna valores. Apenas exibe o resultado da validação de integridade no terminal. 
    """
    
    print("\n" + "="*60)
    print("VALIDAÇÃO DE INTEGRIDADE")
    print("="*60)
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM votos")
    total_votos = cursor.fetchone()[0]
    
    try:
        cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 'Já Votou'")
        total_status = cursor.fetchone()[0]
    except:
        total_status = 0
    
    print(f"Total de votos registrados na urna           : {total_votos}")
    print(f"Quantidade de eleitores com status 'Já Votou': {total_status}")
    print("-"*60)
    
    if total_votos == total_status:
        print("✅ INTEGRIDADE CONFIRMADA: A eleição foi íntegra!")
    else:
        print("❌ ALERTA DE INCONSISTÊNCIA: Divergência detectada entre votos e eleitores!")
        
    cursor.close()
    conexao.close()
    print("="*60)


if __name__ == "__main__":
    exibir_boletim_urna_completo()
    mostrar_comparecimento()
    mostrar_partidos()
    mostrar_integridade()