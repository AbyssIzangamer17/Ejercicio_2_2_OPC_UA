import asyncio
import random
from asyncua import ua, Server

async def main():
    # Configuración del servidor
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")
    
    # Configurar el espacio de nombres
    uri = "http://izan.urios.industrial"
    idx = await server.register_namespace(uri)

    # Crear objetos y variables
    myobj = await server.nodes.objects.add_object(idx, "SensorPlanta1")
    temp = await myobj.add_variable(idx, "Temperatura", 0.0)
    pres = await myobj.add_variable(idx, "Presion", 1.0)
    
    # Hacer variables escribibles para el cliente (opcional)
    await temp.set_writable()
    await pres.set_writable()

    print("Servidor OPC-UA iniciado en opc.tcp://localhost:4840")
    
    async with server:
        while True:
            # Simular cambios en los datos
            new_temp = 20.0 + random.uniform(-2, 2)
            new_pres = 1.0 + random.uniform(-0.1, 0.1)
            
            await temp.write_value(new_temp)
            await pres.write_value(new_pres)
            
            print(f"Temperatura: {new_temp:.2f} | Presión: {new_pres:.2f}")
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
