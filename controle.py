import sqlite3
from sqlite3 import Error
con = sqlite3.connect('locadora.db')
c = con.cursor()

class Controle_DB():
    def __init__(self):
        pass


    def criar_tabela_filme(self):
        c.execute('''
            CREATE TABLE IF NOT EXISTS filme(
                imdb text not null primary key,
                titulo_or text,
                titulo_br text,
                ano text,
                duracao_min text,
                idioma text,
                genero text,
                direcao text,
                roteiro text,
                classificacao text,
                pais text,
                disponibilidade text
            )
        ''')

    def criar_tabela_cliente(self):
        c.execute('''
            CREATE TABLE IF NOT EXISTS cliente(
                cpf text not null primary key,
                nome text,
                data_nascimento text,
                endereco_rua text,
                endereco_numero text,
                endereco_bairro text,
                telefone text,
                email text,
                situacao text
            )
        ''')

    def criar_tabela_aluguel(self):
        c.execute('''
            CREATE TABLE IF NOT EXISTS aluguel(
                cpf text,
                imdb text,
                situacao_aluguel text,
                data_inicio text,
                data_fim text,
                FOREIGN KEY(cpf) REFERENCES cliente(cpf),
                FOREIGN KEY(imdb) REFERENCES filme(imdb)
            )
        ''')

    def inserir(self, tabela, valores):
        c.execute(f'INSERT INTO {tabela} VALUES {valores}')
        con.commit()
    
    def editar(self, tabela, campoModificado, novoValor, campoComparacao, valorComparacao):
        c.execute(f'''
            UPDATE {tabela}
            SET {campoModificado} = ?
            WHERE {campoComparacao} = ?
        ''', (novoValor, valorComparacao))
        
        con.commit()

    def editarComposto(self, tabela, campoModificado, novoValor, campoComparacao, valorComparacao):
        c.execute(f'''
            UPDATE {tabela}
            SET {campoModificado} = ?
            WHERE {campoComparacao} = ? and situacao_aluguel = 'aberto'
        ''', (novoValor, valorComparacao))
        con.commit()

    
    def consultar(self, consulta, tabela, campo, valorCampo):
        a = c.execute(f'SELECT {consulta} FROM {tabela} WHERE {campo} = {valorCampo}').fetchall()
        return a

    def consultaMultipla(self, consulta, tabela, campo, valorCampo, campo2):
        a = c.execute(f'SELECT {consulta} FROM {tabela} WHERE {campo} = {valorCampo} or {campo2} = {valorCampo}').fetchall()
        return a
    
    def consultarTudo(self, tabela):
        a = c.execute(f'SELECT * FROM {tabela}').fetchall()
        return a

    def excluir(self, tabela, campoComparacao, valorComparacao):
        c.execute(f'DELETE FROM {tabela} WHERE {campoComparacao} = {valorComparacao}')
        con.commit()
    
    def qntdRegistros(self, coluna, tabela):
        a = c.execute(f'SELECT COUNT({coluna}) FROM {tabela}').fetchall()
        return a[0][0]
    
    def verificarDisponibilidadeFilme(self, imdb):
        a = c.execute(f'SELECT disponibilidade FROM filme WHERE imdb = {imdb}').fetchall()
        return a[0][0]

    def verificarSituacaoCliente(self, cpf):
        a = c.execute(f'SELECT situacao FROM cliente WHERE cpf = {cpf}').fetchall()
        return a[0][0]
    
    