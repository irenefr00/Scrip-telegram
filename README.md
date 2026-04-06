Integración de Wazuh con Telegram API
Este script en Python permite el envío de alertas críticas desde un gestor de Wazuh hacia un bot de Telegram en tiempo real.

Instalación en el Servidor
Mover el script a /var/ossec/integrations/.

Dar permisos: chmod 750 y chown root:wazuh.

Configurar el bloque <integration> en el ossec.conf.
