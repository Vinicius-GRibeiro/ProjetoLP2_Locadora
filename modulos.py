import utilidades as u
from colorama import Fore, Style, Back, init, deinit
from sqlite3 import Error
from controle import Controle_DB
from aluguel_modelo import Aluguel
from cliente_modelo import Cliente
from filme_modelo import Filme
from datetime import datetime, timedelta

cb = Controle_DB()

def menuPrincipal():
    u.limparTela()

    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 MENU PRINCIPAL \U00002753 ==============={Style.RESET_ALL}\n')
    print(f'\t\t  {Fore.YELLOW}{Style.BRIGHT}1{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Aluguel{Style.RESET_ALL}')
    print(f'\t\t  {Fore.YELLOW}{Style.BRIGHT}2{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Clientes{Style.RESET_ALL}')
    print(f'\t\t  {Fore.YELLOW}{Style.BRIGHT}3{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Filmes{Style.RESET_ALL}')
    print(f'\t\t  {Fore.YELLOW}{Style.BRIGHT}4{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Sair{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}____________________________________________________{Style.RESET_ALL}')
    op = input('\U0001F449 ')
    return op

def MP1_Aluguel():
    while True:
        op = submenu('aluguel')
        if op == '1':
            if cb.qntdRegistros('cpf', 'cliente') != 0 and cb.qntdRegistros('imdb', 'filme') != 0:
                if MP1_Aluguel_novo(): break
            else:
                u.limparTela()
                print(f'{Fore.RED}Para realizar um novo aluguel, você deve cadastrar primeiro um {Style.BRIGHT}cliente{Style.NORMAL} e um {Style.BRIGHT}filme{Style.RESET_ALL}')
                u.pressEnter()
        elif op == '2':
            MP1_Aluguel_consultar()
        elif op == '3':
            MP1_Aluguel_editar()
        elif op == '4':
            u.limparTela()
            print(f'{Back.RED}Impossível excluir registro de aluguel{Style.RESET_ALL}\n')
            u.pressEnter()
        elif op == '5':
            break
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
            u.pressEnter()

def MP2_Clientes():
    while True:
        op = submenu('cliente')
        if op == '1': #Novo
            
            u.limparTela()
            if MP2_Clientes_novo(): break

        elif op == '2': #Consultar
            MP2_Clientes_consultar()
        elif op == '3': #Editar
            MP2_Clientes_editar()
        elif op == '4': #Excluir
            MP2_Clientes_excluir()
        elif op == '5':
            break
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
            u.pressEnter()

def MP3_Filmes():
    while True:
        op = submenu('filme')
        if op == '1':
            u.limparTela()
            if MP3_Filmes_novo(): break
        elif op == '2':
            MP3_Filmes_consultar()
        elif op == '3':
            MP3_Filmes_editar()
        elif op == '4':
            MP3_Filmes_excluir()
        elif op == '5':
            break
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
            u.pressEnter()



def submenu(tabela):
    u.limparTela()

    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 {str(tabela).upper()} \U00002753 ==============={Style.RESET_ALL}\n')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}1{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Novo {tabela}{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}2{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar {tabela}{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}3{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Editar {tabela}{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}4{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Excluir {tabela}{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}5{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Voltar{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}____________________________________________________{Style.RESET_ALL}')
    op = input('\U0001F449 ')
    return op



def verificarCPF(cpf):
    cpfNeg = cpf[::-1]
    for i in range(2, 0, -1):
        cpfEnum = enumerate(cpfNeg[i:], start=2)
        digVerificador = sum(map(lambda x: int(x[1]) * x[0], cpfEnum)) * 10 % 11
        if cpfNeg[i - 1:i] != str(digVerificador % 10):
            return False
    return True

def verificarVazio(valor, campo):
    if len(valor) == 0: print(f'{Fore.RED}O campo {campo} é obrigatório{Style.RESET_ALL}\n')
    else: return True



def MP2_Clientes_novo():
    while True:
        u.limparTela()
        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}INFORMAÇÕES DO CLIENTE{Style.NORMAL}-------=======\n{Style.RESET_ALL}')

        while True:
            cpf = input(f'{Style.BRIGHT}{Fore.GREEN}CPF (Sem pontos e traços): {Style.RESET_ALL}')
            if cpf.find('.') == -1 and cpf.find('-') == -1:
                if len(cpf) == 11:
                    if verificarCPF(cpf): break
                    else: print(f'{Fore.RED}CPF Inválido!{Style.RESET_ALL}\n')
                else: print(f'{Fore.RED}O CPF deve conter {Style.BRIGHT}11 números{Style.NORMAL}. Sem traços e nem pontos.{Style.RESET_ALL}\n')
            else: print(f'{Fore.RED}O CPF deve conter {Style.BRIGHT}apenas números{Style.NORMAL}. Sem traços e nem pontos.{Style.RESET_ALL}\n')

        while True:
            nome = input(f'{Style.BRIGHT}{Fore.GREEN}Nome: {Style.RESET_ALL}')
            if verificarVazio(nome, 'nome'): break

        while True:
            dataNasc = input(f'{Style.BRIGHT}{Fore.GREEN}Data de nascimento (DD/MM/AAAA): {Style.RESET_ALL}')
            if verificarVazio(dataNasc, 'data de nascimento'): 
                if len(dataNasc) == 10 and dataNasc.find('/') != -1: break
                else: print(f'{Fore.RED}A data deve estar no formado {Style.BRIGHT}DD/MM/AAAA{Style.NORMAL}. Dois digitos para o dia, dois para o mês e 4 para o ano, separados por uma {Style.BRIGHT}barra /{Style.RESET_ALL}\n')

        while True:
            rua = input(f'{Style.BRIGHT}{Fore.GREEN}Rua: {Style.RESET_ALL}')
            if verificarVazio(rua, 'rua'): break

        while True:
            numero = input(f'{Style.BRIGHT}{Fore.GREEN}Número: {Style.RESET_ALL}')
            if verificarVazio(numero, 'número'): break

        while True:
            bairro = input(f'{Style.BRIGHT}{Fore.GREEN}Bairro: {Style.RESET_ALL}')
            if verificarVazio(bairro, 'bairro'): break

        while True:
            telefone = input(f'{Style.BRIGHT}{Fore.GREEN}Telefone: {Style.RESET_ALL}')
            if verificarVazio(telefone, 'telefone'):
                if len(telefone) == 11: break
                else: print(f'{Fore.RED}O número deve conter 11 digitos, sem espaços.{Style.RESET_ALL}\n')

        while True:
            email = input(f'{Style.BRIGHT}{Fore.GREEN}E-mail: {Style.RESET_ALL}')
            if verificarVazio(rua, 'e-mail'):
                if email.find('@') != -1 and len(email) >= 7: break
                else: print(f'{Fore.RED}E-mail inválido.{Style.RESET_ALL}\n')
            
        u.limparTela()

        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}REVISÃO{Style.NORMAL}-------=======\n{Style.RESET_ALL}')
        print(f'{Style.BRIGHT}{Fore.GREEN}CPF: {Style.RESET_ALL}{cpf}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Nome: {Style.RESET_ALL}{nome}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Data de nascimento: {Style.RESET_ALL}{dataNasc}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Rua: {Style.RESET_ALL}{rua}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Número: {Style.RESET_ALL}{numero}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Bairro: {Style.RESET_ALL}{bairro}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Telefone: {Style.RESET_ALL}{telefone}\n')
        op = input(f'{Style.BRIGHT}Os dados estão corretos? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] (Digite 0 para cancelar)').upper()
        if op == 'S' or op == '0': break

    if op == '0': return True
    else:
        c = Cliente(cpf, nome, dataNasc, rua, numero, bairro, telefone, email)
        try:
            cb.inserir('cliente', c.getAll())
        except Error as e:
            u.limparTela()
            print(f'{Back.RED}Erro ao inserir dados na tabela {Style.BRIGHT}CLIENTE{Style.RESET_ALL}\n{e}\n')
            u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.GREEN}Novo cliente inserido com sucesso{Style.RESET_ALL}\n')
            u.pressEnter()

def MP3_Filmes_novo():
    while True:
        u.limparTela()
        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}INFORMAÇÕES DO FILME{Style.NORMAL}-------=======\n{Style.RESET_ALL}')

        while True:
            imdb = input(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}')
            if verificarVazio(imdb, 'imdb'): break

        while True:
            titulo_ori = input(f'{Style.BRIGHT}{Fore.GREEN}Título original: {Style.RESET_ALL}')
            if verificarVazio(titulo_ori, 'titulo_or'): break

        while True:
            titulo_br = input(f'{Style.BRIGHT}{Fore.GREEN}Título brasileiro: {Style.RESET_ALL}')
            if verificarVazio(titulo_br, 'titulo_br'): break

        while True:
            ano = input(f'{Style.BRIGHT}{Fore.GREEN}Ano: {Style.RESET_ALL}')
            if verificarVazio(ano, 'ano'): break

        while True:
            duracao = input(f'{Style.BRIGHT}{Fore.GREEN}Duração (min.): {Style.RESET_ALL}')
            if verificarVazio(duracao, 'duração'): break

        while True:
            idioma = input(f'{Style.BRIGHT}{Fore.GREEN}Idioma: {Style.RESET_ALL}')
            if verificarVazio(idioma, 'idioma'): break

        while True:
            genero = input(f'{Style.BRIGHT}{Fore.GREEN}Gênero: {Style.RESET_ALL}')
            if verificarVazio(genero, 'gênero'): break

        while True:
            direcao = input(f'{Style.BRIGHT}{Fore.GREEN}Direção: {Style.RESET_ALL}')
            if verificarVazio(direcao, 'direção'): break

        while True:
            roteiro = input(f'{Style.BRIGHT}{Fore.GREEN}Roteiro: {Style.RESET_ALL}')
            if verificarVazio(roteiro, 'roteiro'): break

        while True:
            classificacao = input(f'{Style.BRIGHT}{Fore.GREEN}Classificação: {Style.RESET_ALL}')
            if verificarVazio(classificacao, 'classificação'): break

        while True:
            pais = input(f'{Style.BRIGHT}{Fore.GREEN}País de origem: {Style.RESET_ALL}')
            if verificarVazio(pais, 'país de origem'): break

            
        u.limparTela()

        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}REVISÃO{Style.NORMAL}-------=======\n{Style.RESET_ALL}')
        print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{imdb}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Título Original: {Style.RESET_ALL}{titulo_ori}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Título BR: {Style.RESET_ALL}{titulo_br}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Ano: {Style.RESET_ALL}{ano}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Duração (min.): {Style.RESET_ALL}{duracao}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Idioma: {Style.RESET_ALL}{idioma}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Gênero: {Style.RESET_ALL}{genero}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Direção: {Style.RESET_ALL}{direcao}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Roteiro: {Style.RESET_ALL}{roteiro}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Classificação: {Style.RESET_ALL}{classificacao}')
        print(f'{Style.BRIGHT}{Fore.GREEN}País: {Style.RESET_ALL}{pais}')
        
        op = input(f'{Style.BRIGHT}Os dados estão corretos? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] (Digite 0 para cancelar)').upper()
        
        if op == 'S' or op == '0': break

    if op == '0': return True
    else:
        f = Filme(imdb, titulo_ori, titulo_br, ano, duracao, idioma, genero, direcao, roteiro, classificacao, pais)
        try:
            cb.inserir('filme', f.getAll())
        except Error as e:
            u.limparTela()
            print(f'{Back.RED}Erro ao inserir dados na tabela {Style.BRIGHT}FILME{Style.RESET_ALL}\n{e}\n')
            u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.GREEN}Novo filme inserido com sucesso{Style.RESET_ALL}\n')
            u.pressEnter()

def MP1_Aluguel_novo():
    while True:
        u.limparTela()
        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}INFORMAÇÕES DO ALUGUEL{Style.NORMAL}-------=======\n{Style.RESET_ALL}')

        while True:
            cpf = input(f'{Style.BRIGHT}{Fore.GREEN}CPF do cliente: {Style.RESET_ALL}')
            if verificarVazio(cpf, 'cpf do cliente'): break
        
        while True:
            imdb = input(f'{Style.BRIGHT}{Fore.GREEN}IMDB do filme: {Style.RESET_ALL}')
            if verificarVazio(imdb, 'imdb do filme'): break
        
        while True:
            dataInicio = input(f'{Style.BRIGHT}{Fore.GREEN}Data do aluguel (DD/MM/AAAA): {Style.RESET_ALL}')
            if verificarVazio(dataInicio, 'data inicio'): 
                if len(dataInicio) == 10 and dataInicio.find('/') != -1: break
                else: print(f'{Fore.RED}A data deve estar no formado {Style.BRIGHT}DD/MM/AAAA{Style.NORMAL}. Dois digitos para o dia, dois para o mês e 4 para o ano, separados por uma {Style.BRIGHT}barra /{Style.RESET_ALL}\n')
        
        while True:
            dias = input(f'{Style.BRIGHT}{Fore.GREEN}Tempo do aluguel em dias: {Style.RESET_ALL}')
            if verificarVazio(dias, 'tempo do aluguel em dias'): break
            
        dataFim = datetime.strptime(dataInicio.replace('/','-'), '%d-%m-%Y').date() + timedelta(int(dias))
        dataFim = str(dataFim)


        u.limparTela()

        print(f'{Fore.LIGHTCYAN_EX}=======-------{Style.BRIGHT}REVISÃO{Style.NORMAL}-------=======\n{Style.RESET_ALL}')
        print(f'{Style.BRIGHT}{Fore.GREEN}CPF do cliente: {Style.RESET_ALL}{cpf}')
        print(f'{Style.BRIGHT}{Fore.GREEN}IMDB do filme: {Style.RESET_ALL}{imdb}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Data do início: {Style.RESET_ALL}{dataInicio}')
        print(f'{Style.BRIGHT}{Fore.GREEN}Data do fim: {Style.RESET_ALL}{dataFim}')
        
        op = input(f'{Style.BRIGHT}Os dados estão corretos? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] (Digite 0 para cancelar)').upper()
        
        if op == 'S' or op == '0': break

    if op == '0': return True
    else:
        a = Aluguel(cpf, imdb, dataInicio, dataFim)
        if cb.verificarDisponibilidadeFilme(imdb) == '1':
            if cb.verificarSituacaoCliente(cpf) == '1':
                a.setDisponibilidade = '0'
                try:
                    cb.inserir('aluguel', a.getAll())
                    cb.editar('filme','disponibilidade', '0', 'imdb', imdb)
                except Error as e:
                    u.limparTela()
                    print(f'{Back.RED}Erro ao inserir dados na tabela {Style.BRIGHT}ALUGUEL{Style.RESET_ALL}\n{e}\n')
                    u.pressEnter()
                else:
                    u.limparTela()
                    print(f'{Fore.GREEN}Aluguel realizado com sucesso{Style.RESET_ALL}')
                    u.pressEnter()
            else:
                u.limparTela()
                print(f'{Fore.RED}Cadastro do cliente bloqueado.{Style.RESET_ALL}\n')
                u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.RED}Filme escolhido está indisponível{Style.RESET_ALL}\n')
            u.pressEnter()

def MP2_Clientes_consultar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 CONSULTAR \U00002753 ==============={Style.RESET_ALL}\n')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}1{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar tudo{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}2{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar por cpf{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}==============================================={Style.RESET_ALL}\n')
    op = input('\U0001F449 ')

    u.limparTela()
    if op == '1':
        itens = cb.consultarTudo('cliente')
        for a in itens:
            print(f'{Style.BRIGHT}{Fore.GREEN}CPF: {Style.RESET_ALL}{a[0]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[1]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Situação: {Style.RESET_ALL}{a[2]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Data início: {Style.RESET_ALL}{a[3]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Data fim: {Style.RESET_ALL}{a[4]}\n')

        u.pressEnter()
    elif op == '2':
        cpf = input(f'\t\t{Fore.YELLOW}{Style.BRIGHT}{Style.NORMAL}{Fore.LIGHTCYAN_EX}Informe o CPF\n\U0001F449 {Style.RESET_ALL}')
        itens = cb.consultar('*', 'cliente', 'cpf', cpf)
        
        if len(itens) != 0:

            u.limparTela()
            for a in itens:
                print(f'{Style.BRIGHT}{Fore.GREEN}CPF: {Style.RESET_ALL}{a[0]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[1]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Situação: {Style.RESET_ALL}{a[2]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Data início: {Style.RESET_ALL}{a[3]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Data fim: {Style.RESET_ALL}{a[4]}\n')
            
            u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Não existe nenhum cliente cadastrado com o CPF informado{Style.RESET_ALL}')
            u.pressEnter()

    else:
        u.limparTela()
        print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
        u.pressEnter()

def MP3_Filmes_consultar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 CONSULTAR \U00002753 ==============={Style.RESET_ALL}\n')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}1{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar tudo{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}2{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar por IMDB{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}==============================================={Style.RESET_ALL}\n')
    op = input('\U0001F449 ')

    u.limparTela()

    if op == '1':
        itens = cb.consultarTudo('filme')
        for a in itens:
            print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[0]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Titulo original: {Style.RESET_ALL}{a[1]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Título brasileiro: {Style.RESET_ALL}{a[2]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Ano: {Style.RESET_ALL}{a[3]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Duração: {Style.RESET_ALL}{a[4]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Idioma: {Style.RESET_ALL}{a[5]} minutos')
            print(f'{Style.BRIGHT}{Fore.GREEN}Gênero: {Style.RESET_ALL}{a[6]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Direção: {Style.RESET_ALL}{a[7]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Roteiro: {Style.RESET_ALL}{a[8]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Classificação: {Style.RESET_ALL}{a[9]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}País: {Style.RESET_ALL}{a[10]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Disponibilidade: {Style.RESET_ALL}{a[11]}\n')


        u.pressEnter()
    elif op == '2':
        imdb = input(f'\t\t{Fore.YELLOW}{Style.BRIGHT}{Style.NORMAL}{Fore.LIGHTCYAN_EX}Informe o IMDB\n\U0001F449 {Style.RESET_ALL}')
        itens = cb.consultar('*', 'filme', 'imdb', imdb)

        if len(itens) != 0:
            u.limparTela()
            for a in itens:
                print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[0]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Titulo original: {Style.RESET_ALL}{a[1]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Título brasileiro: {Style.RESET_ALL}{a[2]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Ano: {Style.RESET_ALL}{a[3]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Duração: {Style.RESET_ALL}{a[4]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Idioma: {Style.RESET_ALL}{a[5]} minutos')
                print(f'{Style.BRIGHT}{Fore.GREEN}Gênero: {Style.RESET_ALL}{a[6]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Direção: {Style.RESET_ALL}{a[7]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Roteiro: {Style.RESET_ALL}{a[8]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Classificação: {Style.RESET_ALL}{a[9]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}País: {Style.RESET_ALL}{a[10]}\n')
                print(f'{Style.BRIGHT}{Fore.GREEN}Disponibilidade: {Style.RESET_ALL}{a[11]}')
            u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Não existe nenhum filme cadastrado com o IMDB informado{Style.RESET_ALL}')
            u.pressEnter()
    else:
        u.limparTela()
        print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
        u.pressEnter()

def MP1_Aluguel_consultar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 CONSULTAR \U00002753 ==============={Style.RESET_ALL}\n')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}1{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar tudo{Style.RESET_ALL}')
    print(f'\t\t{Fore.YELLOW}{Style.BRIGHT}2{Style.NORMAL} {Fore.LIGHTCYAN_EX}- Consultar por IMDB ou CPF{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}==============================================={Style.RESET_ALL}\n')
    op = input('\U0001F449 ')

    u.limparTela()

    if op == '1':
        valor = cb.consultarTudo('aluguel')
        for a in valor:
            print(f'{Style.BRIGHT}{Fore.GREEN}CPF: {Style.RESET_ALL}{a[0]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[1]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Situação: {Style.RESET_ALL}{a[2]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Data de início: {Style.RESET_ALL}{a[3]}')
            print(f'{Style.BRIGHT}{Fore.GREEN}Data do fim: {Style.RESET_ALL}{a[4]}\n')
        u.pressEnter()
    elif op == '2':
        valor = input(f'\t\t{Fore.YELLOW}{Style.BRIGHT}{Style.NORMAL}{Fore.LIGHTCYAN_EX}Informe o IMDB ou CPF\n\U0001F449 {Style.RESET_ALL}')
        itens = cb.consultaMultipla('*', 'aluguel', 'imdb', valor,'cpf')

        if len(itens) != 0:
            u.limparTela()
            for a in itens:
                print(f'{Style.BRIGHT}{Fore.GREEN}CPF: {Style.RESET_ALL}{a[0]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}IMDB: {Style.RESET_ALL}{a[1]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Situação: {Style.RESET_ALL}{a[2]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Data de início: {Style.RESET_ALL}{a[3]}')
                print(f'{Style.BRIGHT}{Fore.GREEN}Data do fim: {Style.RESET_ALL}{a[4]}\n')
            u.pressEnter()
        else:
            u.limparTela()
            print(f'{Fore.RED}{Style.BRIGHT}Não existe nenhum aluguel cadastrado com o IMDB ou CPF informado{Style.RESET_ALL}')
            u.pressEnter()
    else:
        u.limparTela()
        print(f'{Fore.RED}{Style.BRIGHT}Opção inválida{Style.RESET_ALL}')
        u.pressEnter()

def MP2_Clientes_editar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 ALTERAR CADASTRO \U00002753 ==============={Style.RESET_ALL}\n')
    cpf = input(f'{Fore.YELLOW}{Style.BRIGHT}CPF do cliente\n\U0001F449 {Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}\nCPF | Nome | Data_nascimento | Rua | Número | Bairro | Telefone | Email | Situacao{Style.RESET_ALL}')
    campo = input(f'{Fore.YELLOW}Qual campo deseja alterar? (informe o nome do campo sem acentos)\n\U0001F449 {Style.RESET_ALL}').lower()
    valor = input(f"{Fore.YELLOW}Qual o novo valor do campo '{campo}'\n\U0001F449{Style.RESET_ALL}").lower()
    
    try:
        cb.editar('cliente', campo, valor, 'cpf', cpf)
    except Error as e:
        u.limparTela()
        print(f'{Back.RED}Erro ao editar dados{Style.RESET_ALL}\n{e}\n')
        u.pressEnter()
    else:
        u.limparTela()
        print(f'{Fore.GREEN}Dado alterado com sucesso{Style.RESET_ALL}\n')
        u.pressEnter()

def MP3_Filmes_editar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 ALTERAR CADASTRO \U00002753 ==============={Style.RESET_ALL}\n')
    imdb = input(f'{Fore.YELLOW}{Style.BRIGHT}IMDB do filme\n\U0001F449 {Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}\IMDB | titulo_or | titulo_br | ano | duracao_min | idioma | gênero | direção | roteiro | classificação | pais | disponibilidade{Style.RESET_ALL}')
    campo = input(f'{Fore.YELLOW}Qual campo deseja alterar? (informe o nome do campo sem acentos)\n\U0001F449 {Style.RESET_ALL}').lower()
    valor = input(f"{Fore.YELLOW}Qual o novo valor do campo '{campo}'\n\U0001F449{Style.RESET_ALL}").lower()
    
    try:
        cb.editar('filme', campo, valor, 'imdb', imdb)
    except Error as e:
        u.limparTela()
        print(f'{Back.RED}Erro ao editar dados{Style.RESET_ALL}\n{e}\n')
        u.pressEnter()
    else:
        u.limparTela()
        print(f'{Fore.GREEN}Dado alterado com sucesso{Style.RESET_ALL}\n')
        u.pressEnter()
    
def MP1_Aluguel_editar():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 ALTERAR CADASTRO \U00002753 ==============={Style.RESET_ALL}\n')
    imdb = input(f'{Fore.YELLOW}{Style.BRIGHT}CPF do cliente\n\U0001F449 {Style.RESET_ALL}')
    print(f'{Fore.GREEN}{Style.BRIGHT}CPF | IMDB | Data_inicio | Data_Fim | Situação_aluguel{Style.RESET_ALL}')
    campo = input(f'{Fore.YELLOW}Qual campo deseja alterar? (informe o nome do campo sem acentos)\n\U0001F449 {Style.RESET_ALL}').lower()
    valor = input(f"{Fore.YELLOW}Qual o novo valor do campo '{campo}'\n\U0001F449{Style.RESET_ALL}").lower()
    
    try:
        cb.editarComposto('aluguel', campo, valor, 'cpf', imdb)
    except Error as e:
        u.limparTela()
        print(f'{Back.RED}Erro ao editar dados{Style.RESET_ALL}\n{e}\n')
        u.pressEnter()
    else:
        u.limparTela()
        print(f'{Fore.GREEN}Dado alterado com sucesso{Style.RESET_ALL}\n')
        u.pressEnter()

def MP2_Clientes_excluir():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 EXCLUIR \U00002753 ==============={Style.RESET_ALL}\n')
    cpf = input(f'{Fore.YELLOW}{Style.BRIGHT}CPF do cliente\n\U0001F449 {Style.RESET_ALL}')

    op = input(f'{Style.BRIGHT}Deseja mesmo excluir o cliente? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] ').upper()
    if op == 'S':
        cb.excluir('cliente', 'cpf', cpf)
        u.limparTela()
        print(f'{Fore.GREEN}Cliente removido do sistema{Style.RESET_ALL}\n')
        u.pressEnter()

def MP3_Filmes_excluir():
    u.limparTela()
    print(f'{Fore.GREEN}{Style.BRIGHT}=============== \U00002753 EXCLUIR \U00002753 ==============={Style.RESET_ALL}\n')
    imdb = input(f'{Fore.YELLOW}{Style.BRIGHT}IMDB do filme\n\U0001F449 {Style.RESET_ALL}')

    op = input(f'{Style.BRIGHT}Deseja mesmo excluir o filme? {Style.RESET_ALL}[{Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] ').upper()
    if op == 'S':
        cb.excluir('filme', 'imdb', imdb)
        u.limparTela()
        print(f'{Fore.GREEN}Filme removido do sistema{Style.RESET_ALL}\n')
        u.pressEnter()