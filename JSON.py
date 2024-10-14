printar = 0

for printar in range(1, 145):  # começa em 1 e vai até 5
    print("
          {
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
                "value": null
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
        "h": 3,
        "w": 1,
        "x": 0,
        "y": 0
      },
      "id": 1,
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
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
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
            "filter": "camera1"
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
            "count": false,
            "disableDataAlignment": false,
            "showDisabledItems": false,
            "skipEmptyValues": false,
            "useTrends": "default",
            "useZabbixValueMapping": false
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": false
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
      "title": "camera1",
      "type": "stat"
    },")
