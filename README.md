# 🌐 AnyIPTrack - AnyDesk IP Address Resolver 🖥️

**AnyIPTrack** es una herramienta diseñada para monitorizar el proceso de AnyDesk en tu sistema, capturar la dirección IP remota cuando se establece una conexión, y mostrar información geográfica detallada sobre dicha IP. Esta es la primera versión de la herramienta.

## 🛠️ Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio**

    ```sh
   git clone https://github.com/MikeDevQH/AnyDesk-IP-Track.git
   cd AnyDesk-IP-Track
    ```

2. **Instalar las dependencias**

   Las dependencias se instalan automáticamente, pero si hay algun error puedes instalarlas mediante el siguiente comando:

    ```sh
   pip install -r requirements.txt
    ```

## ▶️ Uso

Para ejecutar el programa, simplemente utiliza el siguiente comando:

   ```sh
   python AnyIPTrack.py
   ```

## 🚀 Ejemplo de Salida

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

        ████████╗██████╗  █████╗  ██████╗██╗  ██╗
        ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
           ██║   ██████╔╝███████║██║     █████╔╝
           ██║   ██╔══██╗██╔══██║██║     ██╔═██╗
           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 waiting for connection...
 connection established!
  +------------------+--------------------------------------+
  |   IP         -->   185.107.56.220     
  +------------------+--------------------------------------+
  |   Continent  -->   Europe (EU)
  +------------------+--------------------------------------+
  |   Country    -->   Netherlands (NL)
  +------------------+--------------------------------------+
  |   Region     -->   North Holland (NH)
  +------------------+--------------------------------------+
  |   City       -->   Amsterdam
  +------------------+--------------------------------------+
  |   Timezone   -->   Europe/Amsterdam
  +------------------+--------------------------------------+
  |   Lat        -->   52.3675
  +------------------+--------------------------------------+
  |   Lon        -->   4.9041
  +------------------+--------------------------------------+
  |   ISP        -->   NForce Entertainment B.V.
  +------------------+--------------------------------------+
  |   ORG        -->   ORG-NE3-RIPE
  +------------------+--------------------------------------+
  |   AS         -->   NFORCE (AS43350 NForce Entertainment B.V.)
  +------------------+--------------------------------------+

    [>] Closing AnyIP... # Created by MikeDevQH
Press 'enter' to exit...

  ```
