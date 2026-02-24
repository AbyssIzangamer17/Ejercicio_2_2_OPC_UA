# 🔌 Ejercicio 2.2: Ecosistema OPC-UA Industrial
### Comunicación de Datos Virtuales mediante Arquitectura Cliente-Servidor

Implementación de un sistema de comunicación interoperable basado en el estándar OPC-UA, permitiendo la monitorización en tiempo real de sensores virtuales.

## 🏗️ Arquitectura
1.  **Servidor (`server_opcua.py`)**: Emite datos de temperatura y presión aleatorios en un bus TCP seguro.
2.  **Cliente (`client_opcua.py`)**: Se suscribe a los cambios del servidor y genera alertas de seguridad.

## 🚀 Instrucciones de Uso
1. Iniciar el servidor:
   ```powershell
   python server_opcua.py
   ```
2. Iniciar el cliente en otra terminal:
   ```powershell
   python client_opcua.py
   ```

## 👤 Autor
**Izan Urios** - 3R de Automatización y Robótica Industrial.
