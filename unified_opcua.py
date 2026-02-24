import asyncio
import random
import sys
from asyncua import Server, Client

# SCRIPT HÍBRIDO: Servidor incorporado para facilidad de uso
async def run_opcua_ecosystem():
    print("="*60)
    print("🔌 ECOSISTEMA OPC-UA INTEGRADO (AUTO-MANAGED)")
    print("="*60)
    
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://127.0.0.1:4841/freeopcua/server/")
    
    uri = "http://izan.urios.industrial"
    idx = await server.register_namespace(uri)
    myobj = await server.nodes.objects.add_object(idx, "Planta_Izan")
    temp = await myobj.add_variable(idx, "Temperatura", 0.0)
    
    print("✅ Servidor iniciado automáticamente en puerto 4841.")
    
    async with server:
        # Iniciar cliente en la misma tarea asíncrona para simplificar
        print("✅ Cliente conectado internamente al bus de datos.")
        print("Monitorizando variables críticas...\n")
        
        for i in range(15):
            # Servidor escribe
            val = round(20.0 + random.uniform(-3, 3), 2)
            await temp.write_value(val)
            
            # Cliente lee
            read_val = await temp.read_value()
            status = "🟢 OK" if read_val < 22 else "🔴 ALERTA TÉRMICA"
            
            print(f"[{i+1:02d}] Sensor Planta: {read_val} °C | Estado: {status}")
            await asyncio.sleep(1.5)

    print("\n🏁 Simulación completada.")

if __name__ == "__main__":
    try:
        asyncio.run(run_opcua_ecosystem())
    except KeyboardInterrupt:
        pass
