import re
import yaml

# Função para ler o arquivo de saída do Nmap e extrair informações
def processar_saida_nmap(arquivo_nmap):
    hosts = []
    host_info = None
    
    with open(arquivo_nmap, 'r') as file:
        for linha in file:
            # Detecta um novo host
            host_match = re.search(r'Nmap scan report for (.+)', linha)
            if host_match:
                # Salva o host anterior antes de iniciar um novo
                if host_info:
                    hosts.append(host_info)
                
                # Cria um novo dicionário para o próximo host
                host_info = {
                    'host': host_match.group(1),
                    'ip': host_match.group(1),
                    'ports': []
                }
            
            # Detecta uma linha de porta aberta
            port_match = re.search(r'(\d+)/tcp\s+open\s+(\S+)', linha)
            if port_match and host_info:
                port_info = {
                    'port': int(port_match.group(1)),
                    'state': 'open',
                    'service': port_match.group(2)
                }
                host_info['ports'].append(port_info)
        
        # Adiciona o último host ao final do loop
        if host_info:
            hosts.append(host_info)
    
    return hosts

# Função para salvar os dados em formato YAML
def salvar_em_yaml(dados, caminho_arquivo):
    with open(caminho_arquivo, 'w') as file:
        yaml.dump(dados, file, default_flow_style=False)

# Caminho do arquivo de saída do Nmap e do arquivo YAML de destino
arquivo_nmap = 'nmap.txt'
caminho_arquivo_yaml = 'saida_yaml.yaml'

# Processa o arquivo de saída do Nmap
hosts_encontrados = processar_saida_nmap(arquivo_nmap)
saida_yaml = {'zabbix_export': {'hosts': hosts_encontrados}}

# Salva os resultados no arquivo YAML
salvar_em_yaml(saida_yaml, caminho_arquivo_yaml)

print(f"Processamento concluído. Resultado salvo em {caminho_arquivo_yaml}.")
