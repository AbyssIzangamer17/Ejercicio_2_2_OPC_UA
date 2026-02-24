"""
OPC-UA Cliente Industrial
Autor: Izan Urios | 3R Automatización y Robótica Industrial

Cliente OPC-UA que se conecta al servidor y monitoriza
todas las variables industriales en tiempo real.

Requisitos:
  - Servidor ejecutándose: python server_opcua.py
  - pip install asyncua

Uso: python client_opcua.py [endpoint]
  endpoint por defecto: opc.tcp://localhost:4841/freeopcua/server/
"""
import asyncio
import sys
from datetime import datetime


async def main():
    from asyncua import Client

    # Endpoint configurable por argumento
    default_url = "opc.tcp://localhost:4841/freeopcua/server/"
    url = sys.argv[1] if len(sys.argv) > 1 else default_url

    print("=" * 62)
    print("  ┌─────────────────────────────────────────────────────┐")
    print("  │          CLIENTE OPC-UA INDUSTRIAL                  │")
    print("  │  Izan Urios · 3R Automatización y Robótica          │")
    print("  ├─────────────────────────────────────────────────────┤")
    print(f"  │  Conectando a: {url:<39}│")
    print("  └─────────────────────────────────────────────────────┘")

    async with Client(url=url) as client:
        uri = "http://izan.urios.industrial"
        idx = await client.get_namespace_index(uri)

        # Descubrir nodos del servidor
        print(f"\n  Namespace: {uri} (idx={idx})")
        print("  Descubriendo nodos del servidor...")

        # Sensores
        temp_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Sensores", f"{idx}:Temperatura"])
        pres_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Sensores", f"{idx}:Presion"])
        vel_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Sensores", f"{idx}:VelocidadMotor"])

        # Actuadores
        bomba_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Actuadores", f"{idx}:BombaActiva"])
        valve_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Actuadores", f"{idx}:ValvulaPorcentaje"])

        # Estado
        alarma_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Estado", f"{idx}:AlarmaActiva"])
        modo_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Estado", f"{idx}:ModoOperacion"])

        print("  ✓ 7 nodos descubiertos. Monitorizando...\n")
        print("-" * 62)

        alert_count = 0
        cycle = 0

        while True:
            cycle += 1
            t = await temp_node.read_value()
            p = await pres_node.read_value()
            v = await vel_node.read_value()
            b = await bomba_node.read_value()
            vl = await valve_node.read_value()
            al = await alarma_node.read_value()
            mo = await modo_node.read_value()

            ts = datetime.now().strftime("%H:%M:%S")

            # Alerts
            alerts = []
            if t > 26: alerts.append(f"TEMP:{t:.1f}°C")
            if p > 1.2: alerts.append(f"PRES:{p:.2f}bar")
            if v > 1150: alerts.append(f"VEL:{v:.0f}rpm")
            if al: alerts.append("ALARMA_SERVER")

            if alerts:
                alert_count += 1
                alert_str = " | ".join(alerts)
                print(f"[{ts}] ⚠ ALERTA #{alert_count}: {alert_str}")
            else:
                print(f"[{ts}] ✓ T:{t:.1f}°C P:{p:.2f}bar V:{v:.0f}rpm " +
                      f"Bomba:{'ON' if b else 'OFF'} Válvula:{vl:.0f}% Modo:{mo}")

            # Estadísticas cada 10 ciclos
            if cycle % 10 == 0:
                print(f"         📊 Ciclo {cycle} | Alertas acumuladas: {alert_count}")

            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
