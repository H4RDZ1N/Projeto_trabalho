import re

def filtrar_paragrafos_por_porta(arquivo_entrada, arquivo_saida, porta='8000'):
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()
    
    paragrafos = conteudo.split('\n\n')
    paragrafos_filtrados = []

    for paragrafo in paragrafos:
        if re.search(rf'{porta}/tcp\s+open', paragrafo):
            paragrafos_filtrados.append(paragrafo)

    with open(arquivo_saida, 'w') as f:
        f.write('\n\n'.join(paragrafos_filtrados))


arquivo_entrada = 'nmap.txt'
arquivo_saida = 'tanto_faz.txt'

filtrar_paragrafos_por_porta(arquivo_entrada, arquivo_saida)

print(f"Arquivo filtrado salvo em: {arquivo_saida}")
