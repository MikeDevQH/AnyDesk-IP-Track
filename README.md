# AnyIPTrack 1.0 - AnyDesk IP Address Resolver

**Anny 1.0** es una herramienta diseñada para monitorizar el proceso de AnyDesk en tu sistema, capturar la dirección IP remota cuando se establece una conexión, y mostrar información geográfica detallada sobre dicha IP. Esta es la primera versión de la herramienta.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio**

    ```sh
   git clone https://github.com/MikeDevQH/AnyDesk-IP-Track.git
   cd AnyDesk-IP-Track
    ```

2 **Instalar las dependencias**

   ```sh
  pip install -r requirements.txt
  ```

## Uso

Para ejecutar el programa, simplemente utiliza el siguiente comando:

  ```sh
  python AnyIPTrack.py
  ```

## Ejemplo de Salida

El programa mostrará un banner de bienvenida y comenzará a monitorizar el proceso de AnyDesk. Cuando se establezca una conexión, se capturará la dirección IP remota y se mostrará la información geográfica correspondiente.

  ```yaml
    █████╗ ███╗  ██╗██╗   ██╗██████╗ ███████╗ ██████╗██╗  ██╗
   ██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝
   ███████║██╔██╗██║ ╚████╔╝ ██║  ██║█████╗  ╚█████╗ █████═╝ 
   ██╔══██║██║╚████║  ╚██╔╝  ██║  ██║██╔══╝   ╚═══██╗██╔═██╗ 
   ██║  ██║██║ ╚███║   ██║   ██████╔╝███████╗██████╔╝██║ ╚██╗
   ╚═╝  ╚═╝╚═╝  ╚══╝   ╚═╝   ╚═════╝ ╚══════╝╚═════╝╚═╝  ╚═╝

                  ██╗██████╗               
                  ██║██╔══██╗              
                  ██║██████╔╝              
                  ██║██╔═══╝               
                  ██║██║                   
                  ╚═╝╚═╝                   
                                                     By MikeDevQH
   ██████╗ ███████╗ ██████╗█████╗ ██╗     ██╗   ██╗███████╗██████╗ 
   ██╔══██╗██╔════╝██╔════╝██╔══██╗██║    ██║   ██║██╔════╝██╔══██╗
   ███████║█████╗  ╚█████╗ ██║  ██║██║    ╚██╗ ██╔╝█████╗  ██████╔╝
   ██╔══██║██╔══╝   ╚═══██╗██║  ██║██║     ╚████╔╝ ██╔══╝  ██╔══██╗
   ██║  ██║███████╗██████╔╝╚█████╔╝███████╗ ╚██╔╝  ███████╗██║  ██║
   ╚═╝  ╚═╝╚══════╝╚═════╝  ╚════╝ ╚══════╝  ╚═╝   ╚══════╝╚═╝  ╚═╝
waiting for connection...

connection established!

╔════════════════════════════════════════════╗
║ IP         : 203.0.113.195                 ║
║ Country    : United States                 ║
║ City       : Mountain View                 ║
║ ISP        : Google LLC                    ║
║ Lat        : 37.386                        ║
║ Lon        : -122.0838                     ║
╚════════════════════════════════════════════╝

Press "Enter" to continue...
``` 