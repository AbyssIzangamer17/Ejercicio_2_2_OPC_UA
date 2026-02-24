"""
OPC-UA Industrial System - Servidor + Cliente
Autor: Izan Urios | 3R Automatización y Robótica Industrial

Este módulo implementa la arquitectura completa OPC-UA:
  1. SERVIDOR: Expone variables industriales (Temperatura, Presión, Velocidad)
  2. CLIENTE: Se conecta al servidor, lee datos y genera alertas

Uso:
  Modo Servidor:   python opcua_system.py server
  Modo Cliente:    python opcua_system.py client
  Modo Demo:       python opcua_system.py demo     (inicia ambos)
"""

import asyncio
import random
import sys

# ==================== SERVIDOR OPC-UA ====================
async def run_server():
    from asyncua import Server

    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")

    uri = "http://izan.urios.industrial"
    idx = await server.register_namespace(uri)

    # Crear nodos industriales
    planta = await server.nodes.objects.add_object(idx, "PlantaIndustrial")
    temp = await planta.add_variable(idx, "Temperatura", 22.0)
    pres = await planta.add_variable(idx, "Presion", 1.0)
    vel  = await planta.add_variable(idx, "Velocidad", 1000.0)

    await temp.set_writable()
    await pres.set_writable()
    await vel.set_writable()

    print("=" * 60)
    print("  SERVIDOR OPC-UA INDUSTRIAL")
    print("  Endpoint: opc.tcp://localhost:4841/freeopcua/server/")
    print(f"  Namespace: {uri} (idx={idx})")
    print("  Variables: Temperatura, Presion, Velocidad")
    print("=" * 60)

    async with server:
        while True:
            t = 22.0 + random.uniform(-3, 5)
            p = 1.0 + random.uniform(-0.2, 0.3)
            v = 1000.0 + random.uniform(-200, 200)

            await temp.write_value(round(t, 2))
            await pres.write_value(round(p, 2))
            await vel.write_value(round(v, 0))

            print(f"[SERVER] Temp: {t:.2f}°C | Pres: {p:.2f} bar | Vel: {v:.0f} rpm")
            await asyncio.sleep(1)


# ==================== CLIENTE OPC-UA ====================
async def run_client():
    from asyncua import Client

    url = "opc.tcp://localhost:4841/freeopcua/server/"
    print(f"\n[CLIENT] Conectando a {url}...")

    async with Client(url=url) as client:
        uri = "http://izan.urios.industrial"
        idx = await client.get_namespace_index(uri)

        temp_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Temperatura"])
        pres_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Presion"])
        vel_node = await client.nodes.root.get_child(
            ["0:Objects", f"{idx}:PlantaIndustrial", f"{idx}:Velocidad"])

        print("[CLIENT] Conexión establecida. Monitorizando...\n")

        while True:
            t = await temp_node.read_value()
            p = await pres_node.read_value()
            v = await vel_node.read_value()

            alerts = []
            if t > 25: alerts.append(f"⚠ TEMP ALTA: {t:.2f}°C")
            if p > 1.2: alerts.append(f"⚠ PRES ALTA: {p:.2f} bar")
            if v > 1150: alerts.append(f"⚠ VEL EXCESIVA: {v:.0f} rpm")

            alert_str = " | ".join(alerts) if alerts else "✓ OK"
            print(f"[CLIENT] T:{t:.1f}°C P:{p:.2f}bar V:{v:.0f}rpm → {alert_str}")
            await asyncio.sleep(1)


# ==================== MODO DEMO (Server + Client) ====================
async def run_demo():
    print("=" * 60)
    print("  MODO DEMO: Servidor + Cliente simultáneos")
    print("=" * 60)
    server_task = asyncio.create_task(run_server())
    await asyncio.sleep(2)  # Esperar a que el servidor arranque
    client_task = asyncio.create_task(run_client())
    await asyncio.gather(server_task, client_task)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "demo"

    if mode == "server":
        asyncio.run(run_server())
    elif mode == "client":
        asyncio.run(run_client())
    elif mode == "demo":
        asyncio.run(run_demo())
    else:
        print("Uso: python opcua_system.py [server|client|demo]")
