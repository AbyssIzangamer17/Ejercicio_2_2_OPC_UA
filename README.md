# 📡 OPC-UA Industrial Explorer — Servidor + Cliente

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![asyncua](https://img.shields.io/badge/asyncua-OPC--UA-orange)](https://github.com/FreeOpcUa/opcua-asyncio)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Ejercicio 2.2** — Comunicación industrial OPC-UA con arquitectura servidor/cliente completa.

Este proyecto implementa un **ecosistema OPC-UA completo** con servidor Python, cliente Python y un panel HMI web. El servidor expone variables industriales estándar y puede ser accedido por **cualquier cliente OPC-UA** del mercado (UaExpert, Prosys, Node-RED, SCADA, etc.).

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────┐
│      SERVIDOR OPC-UA        │
│   server_opcua.py           │
│   opc.tcp://0.0.0.0:4841    │
│                             │
│   PlantaIndustrial/         │
│   ├── Sensores/             │
│   │   ├── Temperatura       │
│   │   ├── Presion           │
│   │   └── VelocidadMotor    │
│   ├── Actuadores/           │
│   │   ├── BombaActiva       │
│   │   └── ValvulaPorcentaje │
│   └── Estado/               │
│       ├── AlarmaActiva      │
│       └── ModoOperacion     │
└──────────┬──────────────────┘
           │ OPC-UA TCP
     ┌─────┴──────┐
     │            │
┌────▼────┐  ┌───▼──────────┐
│ CLIENTE  │  │ CUALQUIER    │
│ PYTHON   │  │ CLIENTE      │
│ client_  │  │ OPC-UA       │
│ opcua.py │  │              │
│          │  │ · UaExpert   │
│ Monitor  │  │ · Prosys     │
│ + Alertas│  │ · Node-RED   │
│          │  │ · WinCC      │
│          │  │ · Ignition   │
└──────────┘  └──────────────┘
```

---

## 🚀 Características Principales

### Servidor OPC-UA (`server_opcua.py`)
- **Endpoint abierto**: `opc.tcp://0.0.0.0:4841/freeopcua/server/`
- **SecurityPolicy: None** — Máxima compatibilidad con cualquier cliente.
- **Namespace personalizado**: `http://izan.urios.industrial`
- **Modelo de nodos estructurado**:
  - `PlantaIndustrial/Sensores/` — 3 variables de sensing (Double)
  - `PlantaIndustrial/Actuadores/` — 2 variables de control (Boolean + Double)
  - `PlantaIndustrial/Estado/` — 2 variables de estado (Boolean + String)
- **Variables escribibles**: Los clientes pueden leer **y escribir** cualquier variable.
- **Simulación de proceso**: Genera datos industriales realistas cada segundo.
- **Alarmas automáticas**: Se activan cuando T > 27°C o P > 1.2 bar.

### Cliente OPC-UA (`client_opcua.py`)
- **Endpoint configurable** por argumento de línea de comandos.
- **Descubrimiento de nodos**: Navega la estructura del servidor automáticamente.
- **Monitorización de 7 variables** con alertas en tiempo real.
- **Estadísticas acumulativas** cada 10 ciclos de lectura.
- Alertas configurables para temperatura, presión y velocidad.

### Panel HMI Web (`scada_visual.html`)
- **Diagrama de arquitectura visual**: Muestra la relación Servidor ↔ Clientes.
- **3 gauges principales**: Temperatura, Presión, Velocidad con barras de progreso.
- **3 indicadores extra**: Bomba, Válvula, Alarma.
- **Gráfico de tendencia**: Canvas con 3 líneas de datos en tiempo real.
- **Terminales duales**: Una para logs del servidor, otra para logs del cliente.
- **Configuración**: Endpoint, namespace y frecuencia de muestreo editables.
- **Panel de clientes compatibles**: Lista de software OPC-UA que puede conectarse.
- **Exportación CSV** de todos los logs.

---

## 📊 Variables Expuestas

| Ruta del Nodo | Tipo | Descripción | Rango |
|---------------|------|-------------|-------|
| `Sensores/Temperatura` | Double | Temperatura del proceso (°C) | 19 - 30°C |
| `Sensores/Presion` | Double | Presión del sistema (bar) | 0.8 - 1.3 bar |
| `Sensores/VelocidadMotor` | Double | RPM del motor principal | 800 - 1200 rpm |
| `Actuadores/BombaActiva` | Boolean | Estado de la bomba de lubricación | ON/OFF |
| `Actuadores/ValvulaPorcentaje` | Double | Apertura de la válvula reguladora (%) | 0 - 100% |
| `Estado/AlarmaActiva` | Boolean | Alarma del sistema | ON/OFF |
| `Estado/ModoOperacion` | String | Modo de operación | AUTOMATICO/MANUAL |

---

## 🛠️ Instalación y Uso

### Requisitos
- **Python 3.8+**
- **asyncua**: `pip install asyncua`
- **Navegador moderno** (para el HMI web)

### 1. Instalar dependencias
```bash
pip install asyncua
```

### 2. Iniciar el Servidor
```bash
# Terminal 1
python server_opcua.py
```
El servidor se iniciará y mostrará la estructura de nodos:
```
============================================================
  ┌─────────────────────────────────────────────────────┐
  │          SERVIDOR OPC-UA INDUSTRIAL                 │
  │  Endpoint: opc.tcp://0.0.0.0:4841/freeopcua/server/│
  │  Variables: 7 nodos en 3 carpetas                   │
  └─────────────────────────────────────────────────────┘
  Esperando conexiones de clientes...
```

### 3. Conectar el Cliente Python
```bash
# Terminal 2
python client_opcua.py
```

O con un endpoint personalizado:
```bash
python client_opcua.py opc.tcp://192.168.1.100:4841/freeopcua/server/
```

### 4. Conectar con UaExpert (u otro cliente)
1. Abrir **UaExpert** (o Prosys OPC UA Browser).
2. Crear nueva conexión → `opc.tcp://localhost:4841/freeopcua/server/`
3. Seleccionar SecurityPolicy: **None**.
4. Conectar → Navegar → `Objects/PlantaIndustrial/`
5. Arrastrar variables al panel de monitorización.

### 5. Abrir el HMI Web
```
Abrir scada_visual.html en el navegador
```

---

## 🔌 Clientes Compatibles

| Cliente | Plataforma | Tipo |
|---------|-----------|------|
| **UaExpert** | Windows/Linux | Browse + Monitor + Write |
| **Prosys OPC UA Browser** | Multiplataforma | Browse + Monitor |
| **Node-RED** | Multiplataforma | node-red-contrib-opcua |
| **Python (asyncua)** | Multiplataforma | client_opcua.py incluido |
| **Ignition** | Industrial SCADA | OPC-UA Driver nativo |
| **WinCC (Siemens)** | Industrial HMI | OPC-UA Client |
| **Kepware** | Windows | OPC-UA Driver |

---

## 📁 Estructura del Proyecto

```
Ejercicio_2_2_OPC_UA/
├── server_opcua.py        # Servidor OPC-UA (7 variables, 3 carpetas)
├── client_opcua.py        # Cliente OPC-UA (monitorización + alertas)
├── opcua_system.py        # Modo combinado (server + client + demo)
├── scada_visual.html      # Panel HMI web con arquitectura visual
├── unified_opcua.py       # Script unificado alternativo
├── Documentacion_OPC_UA.docx  # Documentación del protocolo
└── README.md              # Este archivo
```

---

## 🔬 Conceptos Industriales Aplicados

- **OPC-UA (IEC 62541)**: Estándar de comunicación industrial multiplataforma.
- **Modelo de información**: Estructura jerárquica de nodos con tipos definidos.
- **Arquitectura cliente-servidor**: Separación clara entre productor y consumidor de datos.
- **SCADA/HMI**: Interfaz de supervisión con visualización en tiempo real.
- **Alarmas industriales**: Sistema de alertas basado en umbrales configurables.

---

## 👤 Autor

**Izan Urios** — 3R de Automatización y Robótica Industrial

---

## 📄 Licencia

Proyecto de código abierto bajo licencia **MIT**.
