from controle import Controle_DB
from sqlite3 import Error
from colorama import Fore, Style, Back, init, deinit
import utilidades as u
import modulos as m

db = Controle_DB()

init()
u.limparTela()

try:
    db.criar_tabela_filme()
except Error as e:
    print(f'{Back.RED}Erro ao criar tabela {Style.BRIGHT}FILME{Style.RESET_ALL}\n{e}\n')

try:
    db.criar_tabela_cliente()
except Error as e:
    print(f'{Back.RED}Erro ao criar tabela {Style.BRIGHT}CLIENTE{Style.RESET_ALL}\n{e}\n')

try:
    db.criar_tabela_aluguel()
except Error as e:
    print(f'{Back.RED}Erro ao criar tabela {Style.BRIGHT}ALUGUEL{Style.RESET_ALL}\n{e}\n')


u.limparTela()

while True:
    op = m.menuPrincipal()

    if op == '1':
        m.MP1_Aluguel()
    elif op == '2':
        m.MP2_Clientes()
    elif op == '3':
        m.MP3_Filmes()
    elif op == '4':
        u.limparTela()
        op = input(f'{Style.BRIGHT}Deseja mesmo encerrar o programa? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] ').upper()
        if op == 'S':
            u.limparTela()
            print(f'{Style.BRIGHT}{Fore.YELLOW}Programa encerrado{Style.RESET_ALL}')
            break
    else:
        u.limparTela()
        print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
        u.pressEnter()

