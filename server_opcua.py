"""
OPC-UA Servidor Industrial
Autor: Izan Urios | 3R Automatización y Robótica Industrial

Servidor OPC-UA estándar que expone variables industriales.
Cualquier cliente OPC-UA puede conectarse:
  - UaExpert (Unified Automation)
  - Prosys OPC UA Browser
  - Python asyncua Client
  - Node-RED OPC-UA node
  - Cualquier SCADA/HMI compatible OPC-UA

Endpoint: opc.tcp://0.0.0.0:4841/freeopcua/server/
Namespace: http://izan.urios.industrial

Uso: python server_opcua.py
"""
import asyncio
import random
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


async def main():
    from asyncua import Server, ua

    server = Server()
    await server.init()

    # ── Endpoint abierto a cualquier cliente ──
    server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")
    server.set_server_name("Izan Industrial OPC-UA Server")

    # Política de seguridad: None (para máxima compatibilidad)
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

    # ── Namespace ──
    uri = "http://izan.urios.industrial"
    idx = await server.register_namespace(uri)

    # ── Estructura de nodos (modelo de información) ──
    # Carpeta raíz "PlantaIndustrial"
    planta = await server.nodes.objects.add_object(idx, "PlantaIndustrial")

    # Sensores
    sensores = await planta.add_object(idx, "Sensores")
    temp = await sensores.add_variable(idx, "Temperatura", 22.0,
                                        varianttype=ua.VariantType.Double)
    pres = await sensores.add_variable(idx, "Presion", 1.0,
                                        varianttype=ua.VariantType.Double)
    vel = await sensores.add_variable(idx, "VelocidadMotor", 1000.0,
                                       varianttype=ua.VariantType.Double)

    # Actuadores
    actuadores = await planta.add_object(idx, "Actuadores")
    bomba = await actuadores.add_variable(idx, "BombaActiva", False,
                                           varianttype=ua.VariantType.Boolean)
    valve = await actuadores.add_variable(idx, "ValvulaPorcentaje", 50.0,
                                           varianttype=ua.VariantType.Double)

    # Estado del sistema
    estado = await planta.add_object(idx, "Estado")
    alarma = await estado.add_variable(idx, "AlarmaActiva", False,
                                        varianttype=ua.VariantType.Boolean)
    modo = await estado.add_variable(idx, "ModoOperacion", "AUTOMATICO",
                                      varianttype=ua.VariantType.String)

    # Hacer todas las variables escribibles (para que los clientes puedan controlar)
    for var in [temp, pres, vel, bomba, valve, alarma, modo]:
        await var.set_writable()

    print("=" * 62)
    print("  ┌─────────────────────────────────────────────────────┐")
    print("  │          SERVIDOR OPC-UA INDUSTRIAL                 │")
    print("  │  Izan Urios · 3R Automatización y Robótica          │")
    print("  ├─────────────────────────────────────────────────────┤")
    print(f"  │  Endpoint: opc.tcp://0.0.0.0:4841/freeopcua/server/ │")
    print(f"  │  Namespace: {uri}         │")
    print(f"  │  Seguridad: NoSecurity (compatible con todo)       │")
    print("  ├─────────────────────────────────────────────────────┤")
    print("  │  NODOS EXPUESTOS:                                   │")
    print("  │    PlantaIndustrial/                                 │")
    print("  │    ├─ Sensores/                                     │")
    print("  │    │  ├─ Temperatura (Double, °C)                   │")
    print("  │    │  ├─ Presion (Double, bar)                      │")
    print("  │    │  └─ VelocidadMotor (Double, rpm)               │")
    print("  │    ├─ Actuadores/                                   │")
    print("  │    │  ├─ BombaActiva (Boolean)                      │")
    print("  │    │  └─ ValvulaPorcentaje (Double, %)              │")
    print("  │    └─ Estado/                                       │")
    print("  │       ├─ AlarmaActiva (Boolean)                     │")
    print("  │       └─ ModoOperacion (String)                     │")
    print("  └─────────────────────────────────────────────────────┘")
    print()
    print("  Esperando conexiones de clientes...")
    print("  (Conecta con UaExpert, Prosys, client_opcua.py, etc.)")
    print("=" * 62)

    async with server:
        cycle = 0
        while True:
            cycle += 1

            # Simular proceso industrial
            t = 22.0 + random.uniform(-3, 6) + (2 * (cycle % 60 > 30))
            p = 1.0 + random.uniform(-0.15, 0.25)
            v = 1000.0 + random.uniform(-150, 200)

            await temp.write_value(round(t, 2))
            await pres.write_value(round(p, 3))
            await vel.write_value(round(v, 1))

            # Alarma automática
            alarm = t > 27 or p > 1.2
            await alarma.write_value(alarm)

            ts = datetime.now().strftime("%H:%M:%S")
            status = "⚠ ALARMA" if alarm else "✓ OK"
            print(f"[{ts}] T:{t:6.2f}°C  P:{p:5.3f}bar  V:{v:7.1f}rpm  [{status}]")

            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
