from pystyle import *
from colorama import Fore

from Plugins.colors import Palette




class Logger:
    class Success:
        @staticmethod
        def create(value):
            print(f"{Col.light_blue}[{Col.green}+{Col.light_blue}]{Col.light_green} Created{Fore.GREEN}", value)

        @staticmethod
        def delete(value):
            print(f"{Col.light_blue}[{Col.green}+{Col.light_blue}]{Col.light_green} Deleted{Fore.GREEN}", value)

        @staticmethod
        def change(value):
            print(f"{Col.light_blue}[{Col.green}+{Col.light_blue}]{Col.purple} Changed{Fore.LIGHTBLUE_EX}", value)

        @staticmethod
        def success(value):
            print(f"{Col.light_blue}[{Col.green}+{Col.light_blue}]{Fore.GREEN}", value)

    
    class Error:
        @staticmethod
        def create(value):
            print(f"{Col.red}[-]{Fore.RED} Failed to Create{Fore.RED + Fore.YELLOW}", value)

        @staticmethod
        def delete(value):
            print(f"{Col.red}[-]{Fore.RED} Failed to Delete{Fore.RED + Fore.YELLOW}", value)

        @staticmethod
        def change(value):
            print(f"{Col.red}[-]{Fore.RED} Failed to Change{Fore.RED + Fore.YELLOW}", value)
        
        @staticmethod
        def error(value):
            print(f"{Col.red}[-]{Fore.RED + Fore.YELLOW}", value)

    class Log:
        @staticmethod
        def started():
            logo = """
  ██████ ▄▄▄█████▓ ▄▄▄       ██▀███  ▄▄▄█████▓▓█████ ▓█████▄  ▐██▌
▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌ ▐██▌
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ░██   █▌ ▐██▌
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌ ▓██▒
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒  ▒██▒ ░ ░▒████▒░▒████▓  ▒▄▄ 
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒  ░▀▀▒
░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░▒ ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒  ░  ░
░  ░  ░    ░        ░   ▒     ░░   ░   ░         ░    ░ ░  ░     ░
      ░                 ░  ░   ░                 ░  ░   ░     ░   
                                                      ░             
                                                      
                                                      """
            System.Clear()
            print(Palette().red, Center.XCenter(logo))
            print(); print()