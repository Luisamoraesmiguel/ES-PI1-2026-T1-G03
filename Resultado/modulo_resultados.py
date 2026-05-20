from conexao import conectar

def exibir_boletim_urna_completo():
    """RF002.03.02 e RF002.03.03: Listar votos por candidato em ordem alfabética e declarar vencedor"""
    print("\n" + "="*60)
    print("BOLETIM DE URNA")
    print("="*60)
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Buscamos os votos computados
    cursor.execute("SELECT * FROM votos")
    votos = cursor.fetchall()
    
    # Buscamos os candidatos cadastrados para listar em ordem alfabética, cumprindo o edital
    try:
        cursor.execute("SELECT numero_candidato, nome_candidato, partido_candidato FROM candidatos ORDER BY nome_candidato ASC")
        lista_candidatos = cursor.fetchall()
    except:
        # Caso não encontre a tabela candidatos localmente, cria uma lista fictícia de segurança
        lista_candidatos = [("99", "Candidato Nulo/Geral", "PARTIDO")]

    if not votos:
        print("Nenhum voto registrado na urna por enquanto.")
    else:
        # Contabiliza os votos por número
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
    """RF002.03.04: Estatística de Comparecimento com quantidade absoluta e percentual"""
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
    """RF002.03.05: Opção Votos por Partido apresentando a somatória por legenda"""
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
    """RF002.03.06: Opção Validação de Integridade cruzando votos com o status 'Já Votou'"""
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