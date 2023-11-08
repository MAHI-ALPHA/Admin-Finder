#admin finder

import os
import requests 
from urllib import request
from colorama import Fore
import sys


os.system("clear")
print(Fore.GREEN + """
  ================================================================
||                                                                ||
||     /######|  /#####\  /###########\  /###/   /##\  /######\   ||
||    /#######|_/######/ /############/ /###/___/###/   /###/     ||
||   /####/|####/ /###/ /###/    /###/ /### ### ###/   /###/      ||
||  /####/ |###/ /###/ /###/####/###/ /###/   /###/ __/###/__     ||
|| /####/       /###/ /###/    /###/ /###/   /###/ /########/     ||
||                                                        Fsociety||
  ================================================================
""")

try:
    print(Fore.LIGHTYELLOW_EX + "  [*] This is an admin finder")
    x = input(Fore.LIGHTYELLOW_EX + "  [*] Please, Enter your traget just like this (https://www.example.com/): ")
     
    while len(x) == 0 :
        x = input("  [*] Please, Enter your traget just like this (https://www.example.com/): ")
    print("  Checking ...")

except KeyboardInterrupt:
    sys.exit(0)



def ip_finder():
    try:
        dic_file = open("dictionary.txt", "r")
        for aline in dic_file.readlines():
            tmp = aline.split()
            url = x+tmp[0]
            req = requests.head(url)

            if req.status_code == 200 :
                print(Fore.GREEN + "  [+] Find Something [" + url + "]")
            else:
                print(Fore.RED + "  [-] Not Found [" + url + "]")
        dic_file.close()
    except KeyboardInterrupt:
        y = input(Fore.WHITE + " [!]  Are you sure to stop? (yes/no):")

        if y == "yes":
            sys.exit(0)
        else:
            pass
    
ip_finder()
