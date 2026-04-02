import os
from methods.l4 import *
from methods.l7 import *
from Tools.main import *

_0_v1 = "\033[1;31m"
white = "\033[97m"
red = "\033[38;5;196m"
green_hacker = "\033[1;32m"
clear = "\033[0m"
    
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche

          {_0_v1}
                 ╔╗ ╦  ╔═╗╔═╗╦╔═  ╔╗╔╔═╗╔═╗╦ ╦╔═╗
                 ╠╩╗║  ╠═╣║  ╠╩╗  ║║║║ ║║  ╠═╣║╣ 
                 ╚═╝╩═╝╩ ╩╚═╝╩ ╩  ╝╚╝╚═╝╚═╝╩ ╩╚═╝ V1 {clear} 

                 
         Type "{_0_v1}help{clear}" to the view commands

                                                                       >>> {green_hacker}Coded by /@{clear} <<<
""")




def main():
    while True:
        banner()
        select = input(f"""
╔═══[{_0_v1}root{clear}@{_0_v1}/BLCK-N{clear}]
╚══{_0_v1}>{clear} """)
                                        
        if select == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
github.com/BLCK-N {_0_v1}|{clear} t.me/black_noche {_0_v1}|{clear} Discord {_0_v1}|{clear} discord.gg/blacknoche
          {_0_v1}
                    ╦ ╦╔═╗╦  ╔═╗
                    ╠═╣║╣ ║  ╠═╝
                    ╩ ╩╚═╝╩═╝╩ {clear}
                github.com/BLCK-N
        {_0_v1}╔═════════════════════════════════╗{clear}
        {_0_v1}║{clear}  {_0_v1}-{clear} l4     {_0_v1}|{clear} Layer4 Attack Menu  {_0_v1}║{clear}         
        {_0_v1}║{clear}  {_0_v1}-{clear} l7     {_0_v1}|{clear} Layer7 Attack Menu  {_0_v1}║{clear}
        {_0_v1}║{clear}  {_0_v1}-{clear} tools  {_0_v1}|{clear} Tools Menu          {_0_v1}║{clear}
        {_0_v1}║{clear}  {_0_v1}-{clear} update {_0_v1}|{clear} Update /BLCK-N         {_0_v1}║{clear}
        {_0_v1}╚═════════════════════════════════╝{clear}
                                                                       >>> {green_hacker}Coded by /@{clear} <<<
                  """)
            input()


        elif select == "l4":
            layer4()

        
        elif select == "l7":
            layer7()

        elif select == "tools":
            tools()

        elif select == "update":
            os.system("git pull")
            input()

            
    
             


if __name__ == "__main__":
    main()



