#!/usr/bin/env python3
import sys
import requests
import json

# Configuración del bot de Irene
TOKEN = "TUTOKEN"
CHAT_ID = "TUCHATID"

# Leer la alerta de Wazuh
alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extraer información relevante
level = alert_json['rule']['level']
description = alert_json['rule']['description']
agent = alert_json['agent']['name']
rule_id = alert_json['rule']['id']

# Formatear el mensaje para Telegram
message = (
    f" *ALERTA DE SEGURIDAD WAZUH* \n\n"
    f" *Nivel:* {level}\n"
    f" *Agente:* {agent}\n"
    f" *Regla:* {rule_id}\n"
    f"*Descripción:* {description}"
)

# Enviar la notificación
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}
requests.post(url, data=payload)