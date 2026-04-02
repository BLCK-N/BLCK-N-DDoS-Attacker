import requests
import os
import socket
import ipaddress

_0_v1 = "\033[1;31m"
red = "\033[38;5;196m"
green_hacker = "\033[1;32m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
          {_0_v1}
                      ╔╦╗╔═╗╔═╗╦  ╔═╗
                       ║ ║ ║║ ║║  ╚═╗
                       ╩ ╚═╝╚═╝╩═╝╚═╝  {clear}
           {_0_v1}╔═══════════════════════════════════╗{clear}
           {_0_v1}║{clear}  {_0_v1}-{clear} geoip   {_0_v1}|{clear} geolocation ip       {_0_v1}║{clear}         
           {_0_v1}║{clear}  {_0_v1}-{clear} dns     {_0_v1}|{clear} DNS lockup           {_0_v1}║{clear}
           {_0_v1}║{clear}  {_0_v1}-{clear} subnet  {_0_v1}|{clear} Reverse DNS lockup   {_0_v1}║{clear}
           {_0_v1}╚═══════════════════════════════════╝{clear}
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")              
    
def tools():
    while True:
        banner()
        select = input(f"""
╔═══[{_0_v1}root{clear}@{_0_v1}/BLCK-N{clear}]
╚══{_0_v1}>{clear} """)
                                        
        if select.startswith("geoip"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{_0_v1}:{clear} {_0_v1}geoip{clear} <{_0_v1}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def geoip():
                r = requests.get(f"http://ip-api.com/json/{ip}")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
            {_0_v1}╔══════════════════════════════════{clear}
            {_0_v1}║{clear} IP{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("query")}{_0_v1}]{clear}              
            {_0_v1}║{clear} Country{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("country")}{_0_v1}]{clear}        
            {_0_v1}║{clear} Region{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("regionName")}{_0_v1}]{clear}       
            {_0_v1}║{clear} City{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("city")}{_0_v1}]{clear}               
            {_0_v1}║{clear} ISP{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("isp")}{_0_v1}]{clear}        
            {_0_v1}║{clear} Latitude{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("lat")}{_0_v1}]{clear}               
            {_0_v1}║{clear} Longitude{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("lon")}{_0_v1}]{clear}        
            {_0_v1}║{clear} ZIP{_0_v1}:{clear} {_0_v1}[{clear}{r.json().get("zip")}{_0_v1}]{clear}                     
            {_0_v1}╚══════════════════════════════════{clear}                                                                       >>> {green_hacker}Coded by /@{clear} <<<                      """)
                input()

            geoip()

        elif select.startswith("dns"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{_0_v1}:{clear} {_0_v1}dns{clear} <{_0_v1}domain{clear}>")
                input()
                continue

            host = parts[1]

            def dnslockup():
                try:
                    dns = socket.gethostbyname(host)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
            {_0_v1}╔══════════════════════════════════{clear}
            {_0_v1}║{clear} HOST{_0_v1}:{clear} {_0_v1}[{clear}{host}{_0_v1}]{clear}              
            {_0_v1}║{clear} DNS{_0_v1}:{clear} {_0_v1}[{clear}{dns}{_0_v1}]{clear}          
            {_0_v1}╚══════════════════════════════════{clear}                                                                       >>> {green_hacker}Coded by /@{clear} <<<                    """)
                except socket.gaierror:
                    pass
                input()

            dnslockup()


        elif select.startswith("subnet"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{_0_v1}:{clear} {_0_v1}subnet{clear} <{_0_v1}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def subnet():
                try:
                    n = ipaddress.ip_network(ip + "/24", strict=False)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                {_0_v1}╔════════════════════════════════════════════════╗{clear}
                {_0_v1}║{clear} IP       {_0_v1}:{clear} [{ip}]
                {_0_v1}║{clear} SUBNET   {_0_v1}:{clear} [{n}]
                {_0_v1}║{clear} NET ADDR {_0_v1}:{clear} [{n.network_address}]
                {_0_v1}║{clear} BROADCAST{_0_v1}:{clear} [{n.broadcast_address}]
                {_0_v1}║{clear} NETMASK  {_0_v1}:{clear} [{n.netmask}]
                {_0_v1}║{clear} HOSTS    {_0_v1}:{clear} [{n.num_addresses}] addresses
                {_0_v1}╚════════════════════════════════════════════════╝{clear}                                                                       >>> {green_hacker}Coded by /@{clear} <<<                    """)
                except Exception:
                    pass

                input()

            subnet()

if __name__ == "__main__":
    tools()


