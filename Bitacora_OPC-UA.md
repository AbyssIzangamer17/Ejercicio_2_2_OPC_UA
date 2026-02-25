# Bitácora de Desarrollo: OPC-UA Industrial Explorer

## Ejercicio 2.2 — Sistema de Comunicación Cliente-Servidor Industrial

---

### Descripción del Proyecto

El proyecto consiste en crear un ecosistema OPC-UA completo con servidor Python, cliente Python y panel HMI web. El servidor debe exponer variables industriales estándar y ser accesible por cualquier cliente OPC-UA del mercado (UaExpert, Prosys, SCADA, etc.).

---

### Prompts Utilizados

#### Prompt #1
**Prompt:** "El OPC-UA es muy complicado de usar, busca una solución para que sea más sencillo de usar."

**Para qué sirve:** Se creó un script unificado (unified_opcua.py) que combina servidor y cliente en un solo comando, eliminando la necesidad de configurar puertos y procesos separados.

**Corrección:** No — Este prompt fue para simplificar el uso del sistema.

---

#### Prompt #2
**Prompt:** "El OPC-UA no está compuesto por servidor y cliente y debería, arréglalo."

**Para qué sirve:** Se mantuvo la arquitectura separada con server_opcua.py (servidor), client_opcua.py (cliente), y opcua_system.py (script unificado con 3 modos: server, client, demo).

**Corrección:** Sí — Se utilizó para corregir la falta de arquitectura cliente-servidor.

---

#### Prompt #3
**Prompt:** "Del OPC-UA tengo que poder detener simulación, ver los logs, que el texto se lea bien."

**Para qué sirve:** Se implementaron controles en el HMI: botones de INICIAR/DETENER simulación, terminales con logs de alta legibilidad, sistema de logs inteligentes con colores y timestamps, y gráficos de tendencia dinámicos.

**Corrección:** No — Este prompt fue para añadir nuevas funcionalidades de control.

---

#### Prompt #4
**Prompt:** "El OPC-UA que funcione con servidor y cliente. Prepara el OPC-UA para que se pueda conectar a cualquier tipo de cliente."

**Para qué sirve:** Se configuró el servidor para máxima compatibilidad: SecurityPolicy None (máxima compatibilidad), Endpoint opc.tcp://0.0.0.0:4841/freeopcua/server/, namespace personalizado http://izan.urios.industrial, y variables escribibles por cualquier cliente.

**Corrección:** Sí — Este prompt se usó para corregir la arquitectura y asegurar compatibilidad universal con cualquier cliente OPC-UA.

---

#### Prompt #5
**Prompt:** "El SCL está perfecto. Mejora el OPC-UA. Remember that it must have a server and a client."

**Para qué sirve:** Se rediseñó la arquitectura completa: servidor estándar (server_opcua.py) con 7 nodos, cliente separado (client_opcua.py) para monitorización, HMI (scada_visual.html) con diagrama de arquitectura, dos terminales separadas (servidor y cliente), y panel de clientes compatibles listados.

**Corrección:** Sí — Este prompt se usó para corregir y mejorar el OPC-UA manteniendo el SCL intacto.

---

### Resumen de Funcionalidades

| Funcionalidad | Descripción |
|--------------|-------------|
| Servidor OPC-UA | 7 nodos en 3 carpetas (Sensores, Actuadores, Estado) |
| Cliente OPC-UA | Monitorización con alertas en tiempo real |
| HMI Visual | Gráficos, gauges, terminal de logs |
| Gráfico de Tendencia | 3 líneas de datos en tiempo real |
| Exportación CSV | Registro de logs para análisis |
| Compatibilidad Universal | UaExpert, Prosys, Node-RED, SCADA |
| Control de Simulación | Iniciar/Detener desde el HMI |

---

### Variables del Servidor OPC-UA

| Nodo | Tipo | Descripción |
|------|------|-------------|
| Sensores/Temperatura | Double | Temperatura del proceso (°C) |
| Sensores/Presión | Double | Presión del sistema (bar) |
| Sensores/VelocidadMotor | Double | RPM del motor principal |
| Actuadores/BombaActiva | Boolean | Estado de la bomba |
| Actuadores/ValvulaPorcentaje | Double | Apertura de válvula (%) |
| Estado/AlarmaActiva | Boolean | Alarma del sistema |
| Estado/ModoOperacion | String | Modo de operación |

---

### Conclusión

El sistema OPC-UA se consolidó como un ecosistema profesional de comunicación industrial, con arquitectura servidor/cliente real, compatibilidad universal con cualquier cliente OPC-UA, y una interfaz HMI visual que facilita la monitorización y el control.

---

*Documento realizado por Izan Urios — 3R de Automatización y Robótica Industrial*
