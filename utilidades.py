from os import system, name
from colorama import Style, Fore, Back

def limparTela(): system('cls' if name=='nt' else 'clear')

def pressEnter(): input(f'{Style.RESET_ALL}Pressione {Style.BRIGHT}{Fore.GREEN}<ENTER>{Style.RESET_ALL} para continuar...')