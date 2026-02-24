# 🔌 Ejercicio 2.2: Ecosistema OPC-UA Industrial
### Comunicación de Datos Virtuales mediante Arquitectura Cliente-Servidor

## 🚀 Inicio Rápido

1. **Clonar**:
   ```bash
   git clone https://github.com/AbyssIzangamer17/Ejercicio_2_2_OPC_UA.git
   cd Ejercicio_2_2_OPC_UA
   ```

2. **Dependencias**:
   ```powershell
   pip install asyncua
   ```

## 📊 Visualización de Resultados

Para ver el sistema en funcionamiento, usa dos terminales:

1.  **Terminal 1 (Ejecutar Servidor)**:
    ```powershell
    python server_opcua.py
    ```
    *Verás:* "Temperatura: 20.xx | Presión: 1.xx" actualizándose cada 2 seg.

2.  **Terminal 2 (Ejecutar Cliente)**:
    ```powershell
    python client_opcua.py
    ```
    *Verás:* El cliente leyendo esos mismos datos y lanzando **"⚠️ ALERTA"** si la temperatura supera los 21.5°C.

## 👤 Autor
**Izan Urios** - 3R de Automatización y Robótica Industrial.
