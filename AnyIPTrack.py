try:
    import ctypes
    import subprocess, colorama, requests, base64, os, socket
    import sys
    from colorama import Fore, Style
    from pystyle import Center, Colors, Colorate, System, Anime
    import time
except ModuleNotFoundError:
    print("Exception when importing modules")
    print("Installing necessary modules....")
    if os.path.isfile("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip install pystyle")
        os.system("pip install colorama")
        os.system("pip install requests")
    print("Modules installed!")
  
    os._exit(1)

"""
        color
"""
colorama.init()

anydesk_pids = []
anydesk_address = {}
ip_addr = []
old_port = 0
old_ip = ''


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Enjoy")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Enjoy\x07")
    else:
        pass


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    return


def center(var: str, space: int = None):  # From Pycenter
    try:
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2

        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    except OSError:
        print(
            f"{Fore.BLUE}\nStart the program from a normal terminal.\n{Fore.WHITE}If you have any problems you can contact me through my discord (https://discord.com/users/925933412710232105)")
        time.sleep(1)
        os._exit(1)



print(f"                                                                             ")
print(f"                                                                             ")
print(f"{Fore.BLUE}    █████╗ ███╗  ██╗██╗   ██╗██████╗ ███████╗ ██████╗██╗  ██╗")
print(f"   ██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝")
print(f"   ███████║██╔██╗██║ ╚████╔╝ ██║  ██║█████╗  ╚█████╗ █████═╝ ")
print(f"   ██╔══██║██║╚████║  ╚██╔╝  ██║  ██║██╔══╝   ╚═══██╗██╔═██╗ ")
print(f"   ██║  ██║██║ ╚███║   ██║   ██████╔╝███████╗██████╔╝██║ ╚██╗")
print(f"   ╚═╝  ╚═╝╚═╝  ╚══╝   ╚═╝   ╚═════╝ ╚══════╝╚═════╝╚═╝  ╚═╝ ")
print(f"                                                         ")   
print(f"                                                         ")   
print(f"{Fore.BLUE}                      ██╗██████╗ ")
print(f"                      ██║██╔══██╗")
print(f"                      ██║██████╔╝")
print(f"                      ██║██╔═══╝ ")
print(f"                      ██║██║     ")
print(f"                      ╚═╝╚═╝     ")
print(f"{Fore.LIGHTCYAN_EX}                                      By MikeDevQH")
print(f"                                                 ")          
print(f"{Fore.BLUE}        ████████╗██████╗  █████╗  ██████╗██╗  ██╗")                  
print(f"        ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝")                  
print(f"           ██║   ██████╔╝███████║██║     █████╔╝ ")                  
print(f"           ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ")                  
print(f"           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗")                
print(f"           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")  
print(f" {Fore.RED}waiting for connection...")

while 1:
    try:
        if str(subprocess.check_output("tasklist")).count('AnyDesk') <= 3:
            pass
        else:
            for line in str(subprocess.check_output("tasklist")).replace('b"', '"').replace('\\r', '').replace('\\n',
                                                                                                               '\n').split(
                '\n'):
                if 'AnyDesk' in line:
                    try:
                        anydesk_pids.append(line.split('.exe')[1].split()[0].replace(' ', ''))

                    except Exception as e:
                        pass
            nstats_output_lines = str(subprocess.check_output('netstat -p TCP -n -a -o')).replace('b"', '"').replace(
                '\\r', '').replace('\\n', '\n').split('\n')
            for pid in anydesk_pids:
                for line in nstats_output_lines:
                    if pid in line and not 'LISTENING' in line:
                        try:
                            parts = line.split()
                            protocol = parts[0]
                            local_addr = parts[1]
                            remote_addr = parts[2].split(':')[0]
                            remote_port = parts[2].split(':')[1]
                            anydesk_address[remote_addr] = int(remote_port)
                        except Exception as e:
                            print(e)
            for ip, port in anydesk_address.items():
                if int(port) > old_port and not '169.254.' in ip:
                    old_port = int(port)
                    old_ip = ip
            remote_ip = old_ip
            remote_port = old_port
            print(f'{Fore.GREEN} connection established!')


            def ipinfo_command(ip_address):
                """
                Get information about an IP address
                """

                try:
                    socket.inet_pton(socket.AF_INET, ip_address)  # Check the IP address

                    r = requests.get(
                        f'http://ip-api.com/json/{ip_address}?fields=status,message,continentCode,regionName,city,isp,org,as,asname,query')
                    r_json = r.json()

                    if r_json['status'] == 'success':
                        regionName = r_json['regionName']
                        city = r_json['city']
                        isp = r_json['isp']
                        as_ = r_json['as']
                        asname = r_json['asname']


                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")
                        print(f'  {Fore.LIGHTWHITE_EX}|   {Fore.LIGHTBLUE_EX}IP       -->   {Fore.LIGHTCYAN_EX}{remote_ip:<19}')
                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")
                        print(f"  {Fore.LIGHTWHITE_EX}|   {Fore.LIGHTBLUE_EX}Region  -->   {Fore.LIGHTCYAN_EX}{regionName:<19}")
                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")
                        print(f"  {Fore.LIGHTWHITE_EX}|   {Fore.LIGHTBLUE_EX}City     -->   {Fore.LIGHTCYAN_EX}{city:<19}")
                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")
                        print(f"  {Fore.LIGHTWHITE_EX}|   {Fore.LIGHTBLUE_EX}ISP      -->   {Fore.LIGHTCYAN_EX}{isp:<25}")
                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")
                        print(f"  {Fore.LIGHTWHITE_EX}|   {Fore.LIGHTBLUE_EX}AS       -->   {Fore.LIGHTCYAN_EX}{asname} ({Fore.LIGHTBLUE_EX}{as_:<22}{Fore.LIGHTCYAN_EX})")
                        print(f"  {Fore.LIGHTWHITE_EX}+-----------+--------------------------------------+")


                    else:
                        print(
                            f'\n    {Fore.BLUE}[{Fore.LIGHTBLUE_EX}ERR{Fore.LIGHTCYAN_EX}OR{Fore.BLUE}] {Fore.LIGHTCYAN_EX}The IP address is not valid.')

                except requests.exceptions.ConnectionError:
                    print(f'\n    {Fore.BLUE}[{Fore.LIGHTBLUE_EX}ERR{Fore.LIGHTCYAN_EX}OR{Fore.BLUE}] {Fore.LIGHTCYAN_EX}Could not connect to API.')

                except socket.error:
                    print(f'\n    {Fore.BLUE}[{Fore.LIGHTBLUE_EX}ERR{Fore.LIGHTCYAN_EX}OR{Fore.BLUE}] {Fore.LIGHTCYAN_EX}The IP address is not valid.')


            try:
                ipinfo_command(remote_ip)
            except Exception as e:
                print(f'{Fore.LIGHTBLUE_EX}aia. {Fore.LIGHTCYAN_EX + e}')
            print(f'\n\n    {Fore.BLUE}[{Fore.LIGHTBLUE_EX}>{Fore.BLUE}] {Fore.LIGHTWHITE_EX}Closing AnyIP... # Created by {Fore.LIGHTCYAN_EX}MikeDevQH{Fore.RESET}')
            input(Fore.GREEN + 'Press \'enter\' to exit...')
            exit()
    except KeyboardInterrupt:
        print(f'\n\n    {Fore.RED}[{Fore.LIGHTRED_EX}>{Fore.RED}] {Fore.LIGHTWHITE_EX}Closing AnyIP... # Created by {Fore.LIGHTCYAN_EX}MikeDevQH{Fore.RESET}')
        exit()

