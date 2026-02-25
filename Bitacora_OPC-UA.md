# Bitácora de Desarrollo: OPC-UA Industrial Explorer

## Ejercicio 2.2 — Sistema de Comunicación Cliente-Servidor Industrial

---

### Descripción del Proyecto

El proyecto consiste en crear un ecosistema OPC-UA completo con servidor Python, cliente Python y panel HMI web. El servidor debe exponer variables industriales estándar y ser accesible por cualquier cliente OPC-UA del mercado (UaExpert, Prosys, SCADA, etc.).

---

### Prompt de Origen (Contexto General)

**Fuente:** Conversación inicial del proyecto - Antigravity

**Prompt principal del proyecto:**
> "Usa la skill @find-skills para explorar tu ecosistema de 60.000 herramientas y seleccionar, en cada paso, la habilidad más avanzada y adecuada para cumplir este flujo de trabajo:
> Extracción Multimodal: Busca y ejecuta la mejor herramienta de OCR y visión artificial para analizar la imagen/PDF dentro de la carpeta 'PDF DE EJERCICIOS' y extraer las instrucciones de texto.
> Deducción de Objetivos: Si el texto extraído es impreciso o incompleto, busca una skill de agentes autónomos o planificación estratégica capaz de comprender el contexto, deducir el objetivo final del trabajo y 'apañárselas' de forma independiente para descomponer la meta en tareas ejecutables.
> Documentación Académica: Localiza la skill de creación de documentos más robusta que garantice compatibilidad total con LibreOffice. El documento final debe seguir un estilo académico riguroso.
> Estilización y Pie de Página: Identifica una herramienta de diseño de temas o estilización para configurar un pie de página obligatorio con el texto: 'Documento realizado por Izan Urios de 3R de Automatización y Robótica industrial'. Es indispensable que este pie de página incluya un borde superior nítido que lo separe visualmente del cuerpo del documento.
> Ejecuta todo el proceso de forma autónoma, priorizando la precisión técnica y el rigor en el formato final.
> Ve poco a poco y ve diferenciando los ejercicios de forma estructurada y organizada. Haz una carpeta por cada uno y trabaja adecuadamente siendo ordenado."

**Interpretación:** Este prompt establece el flujo de trabajo completo del proyecto. Se buscaba utilizar el ecosistema de habilidades de IA para procesar las instrucciones del PDF y generar una solución organizada y profesional para cada ejercicio.

---

### Prompt de Origen (Ejercicio Específico)

**Fuente:** PDF de Instrucciones del Ejercicio (Captura 2026-02-24)

**Contexto del ejercicio:**
El Ejercicio 2.2 forma parte del bloque "Habilidades del Ecosistema IA" del módulo. Este ejercicio se centra en la comunicación industrial, un pilar fundamental de la automatización moderna.

**Prompt original extraído del PDF:**
> "Exercici 2.2. OPC-UA. Investigar sobre comunicació client-servidor mitjançant OPC-UA."

**Interpretación y desarrollo:**
Este prompt establece como objetivo la investigación sobre comunicación cliente-servidor mediante OPC-UA (Open Platform Communications Unified Architecture). OPC-UA es el estándar de comunicación industrial más robusto y versátil de la actualidad, utilizado en:

- Comunicación PLC-PLC
- Conexión SCADA-HMI
- Integración con sistemas MES/ERP
- Comunicación máquina-a-máquina (M2M)
- IoT industrial

La investigación debe cubrir:
- Fundamentos de OPC-UA (modelo de información, servicios, seguridad)
- Diferencias con OPC Classic (DA)
- Arquitectura cliente-servidor y publisher-subscriber
- Implementaciones populares (UaExpert, Prosys, open62541, asyncua)
- Casos de uso en la industria

**Nota del desarrollo:** El sistema final implementa un ecosistema completo con servidor Python, cliente Python y HMI web visual que permite monitorizar variables industriales en tiempo real y controlar la simulación.

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
