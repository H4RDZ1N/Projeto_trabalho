import json

def create_grafana_dashboard(num_cameras, cameras_per_row=10):
    panels = []
    
    for i in range(num_cameras):
        panel = {
            "datasource": {
                "type": "alexanderzobnin-zabbix-datasource",
                "uid": "bdlzqs8r0nq4gf"
            },
            "fieldConfig": {
                "defaults": {
                    "color": {
                        "mode": "thresholds"
                    },
                    "mappings": [
                        {
                            "options": {
                                "0": {
                                    "color": "dark-red",
                                    "index": 0,
                                    "text": "OFF"
                                },
                                "1": {
                                    "index": 1,
                                    "text": "ON"
                                }
                            },
                            "type": "value"
                        }
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {
                                "color": "dark-red",
                                "value": None
                            },
                            {
                                "color": "dark-green",
                                "value": 1
                            }
                        ]
                    }
                },
                "overrides": []
            },
            "gridPos": {
                "h": 5,
                "w": 1,
                "x": i % cameras_per_row,  # Posição horizontal
                "y": i // cameras_per_row   # Posição vertical
            },
            "id": i + 1,
            "options": {
                "colorMode": "background",
                "graphMode": "none",
                "justifyMode": "center",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": [
                        "lastNotNull"
                    ],
                    "fields": "",
                    "values": False
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True
            },
            "pluginVersion": "11.0.0",
            "targets": [
                {
                    "application": {
                        "filter": ""
                    },
                    "countTriggersBy": "",
                    "datasource": {
                        "type": "alexanderzobnin-zabbix-datasource",
                        "uid": "bdlzqs8r0nq4gf"
                    },
                    "evaltype": "0",
                    "functions": [],
                    "group": {
                        "filter": "RCSG"
                    },
                    "host": {
                        "filter": f"camera{i + 1}"  # Nome da câmera
                    },
                    "item": {
                        "filter": "ICMP: ICMP ping"
                    },
                    "itemTag": {
                        "filter": ""
                    },
                    "macro": {
                        "filter": ""
                    },
                    "options": {
                        "count": False,
                        "disableDataAlignment": False,
                        "showDisabledItems": False,
                        "skipEmptyValues": False,
                        "useTrends": "default",
                        "useZabbixValueMapping": False
                    },
                    "proxy": {
                        "filter": ""
                    },
                    "queryType": "0",
                    "refId": "A",
                    "resultFormat": "time_series",
                    "schema": 12,
                    "table": {
                        "skipEmptyValues": False
                    },
                    "tags": {
                        "filter": ""
                    },
                    "textFilter": "",
                    "trigger": {
                        "filter": ""
                    }
                }
            ],
            "title": f"camera{i + 1}",  # Título do painel
            "type": "stat"
        }
        panels.append(panel)

    dashboard = {
        "annotations": {
            "list": []
        },
        "editable": True,
        "id": None,  # ID do dashboard
        "panels": panels,
        "schemaVersion": 39,
        "tags": [],
        "title": "Cameras Dashboard",
        "uid": "cameras_dashboard",
        "version": 1
    }

    return dashboard

# Criar o documento JSON para 145 câmeras com 25 câmeras por linha
dashboard_data = create_grafana_dashboard(145, cameras_per_row=25)

# Salvar o documento JSON em um arquivo
with open('cameras_dashboard.json', 'w') as json_file:
    json.dump(dashboard_data, json_file, indent=2)

print("Arquivo cameras_dashboard.json criado com sucesso!")
