import asyncio
from asyncua import Client

async def main():
    url = "opc.tcp://localhost:4841/freeopcua/server/"
    async with Client(url=url) as client:
        # El espacio de nombres debe coincidir con el del servidor
        uri = "http://izan.urios.industrial"
        idx = await client.get_namespace_index(uri)

        # Localizar los nodos de interés
        # Nota: La ruta de búsqueda depende de cómo se estructuró en el servidor
        temp_node = await client.nodes.root.get_child(["0:Objects", f"{idx}:SensorPlanta1", f"{idx}:Temperatura"])
        pres_node = await client.nodes.root.get_child(["0:Objects", f"{idx}:SensorPlanta1", f"{idx}:Presion"])

        print(f"Conectado a {url}")
        print("Monitorizando datos industriales en tiempo real...\n")

        for _ in range(10):
            temp_value = await temp_node.read_value()
            pres_value = await pres_node.read_value()
            
            print(f"--- Lectura ---")
            print(f"TERMÓMETRO: {temp_value:.2f} °C")
            print(f"BARÓMETRO: {pres_value:.2f} bar")
            
            if temp_value > 21.5:
                print("⚠️ ALERTA: Temperatura elevada detectada por el agente.")
            
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
