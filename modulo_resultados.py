from conexao import conectar

def mostrar_boletim():
    print("\n== BOLETIM DE URNA ==")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT numero_candidato, nome_candidato, partido_candidato, COUNT(*) FROM votos GROUP BY numero_candidato ORDER BY nome_candidato ASC")
    votos = cursor.fetchall()
    
    if not votos:
        print("Nenhum voto registrado na urna.")
    else:
        vencedor = None
        max_votos = -1
        for v in votos:
            print(f"Candidato: {v[1]} ({v[2]}) | Nº: {v[0]} | Votos: {v[3]}")
            if v[3] > max_votos:
                max_votos = v[3]
                vencedor = v
        print("-" * 40)
        print(f"⭐ VENCEDOR: {vencedor[1]} | Total: {max_votos} votos")
    cursor.close()
    conexao.close()

def mostrar_comparecimento():
    print("\n== ESTATÍSTICA DE COMPARECIMENTO ==")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 'Já Votou'")
    votos = cursor.fetchone()[0]
    
    if total == 0:
        print("Nenhum eleitor cadastrado.")
    else:
        print(f"Total de Eleitores: {total}")
        print(f"Total que Votou: {votos}")
        print(f"Percentual: {(votos/total)*100:.2f}%")
    cursor.close()
    conexao.close()

def mostrar_partidos():
    print("\n== VOTOS POR PARTIDO ==")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT partido_candidato, COUNT(*) FROM votos GROUP BY partido_candidato")
    partidos = cursor.fetchall()
    if not partidos:
        print("Nenhum voto computado.")
    else:
        for p in partidos:
            print(f"Partido: {p[0]} | Votos: {p[1]}")
    cursor.close()
    conexao.close()

def mostrar_integridade():
    print("\n== VALIDAÇÃO DE INTEGRIDADE ==")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM votos")
    votos = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 'Já Votou'")
    status = cursor.fetchone()[0]
    
    print(f"Votos na Urna: {votos} | Eleitores com 'Já Votou': {status}")
    if votos == status:
        print("✅ INTEGRIDADE CONFIRMADA!")
    else:
        print("❌ ALERTA DE INCONSISTÊNCIA!")
    cursor.close()
    conexao.close()

# Executa as opções em sequência para testar tudo de uma vez
if __name__ == "__main__":
    mostrar_boletim()
    mostrar_comparecimento()
    mostrar_partidos()
    mostrar_integridade()