from cliente_modelo import Cliente
from filme_modelo import Filme

class Aluguel(Cliente, Filme):
    def __init__(self, cpf, imdb_filme, data_inicio, data_final):
        #self._id = id
        self._cpf = cpf
        self._imdb_filme = imdb_filme
        self._situacao = 'aberto'
        self._data_inicio = data_inicio
        self._data_final = data_final
    
    #def setId(self, id): self._id = id
    def setCpf(self, cpf): self._cpf = cpf
    def setImdb_filme(self, imdb_filme): self._imdb_filme = imdb_filme
    def setSituacao(self, situacao): self._situacao = situacao
    def setData_inicio(self, data_inicio): self._data_inicio = data_inicio
    def setData_final(self, data_final): self._data_final = data_final

    #def getId(self): return self._id
    def getCpf(self): return self._cpf
    def getImdb_filme(self): return self._imdb_filme
    def getSituacao(self): return self._situacao
    def getData_inicio(self): return self._data_inicio
    def getData_final(self): return self._data_final
    
    def getAll(self):
        all = (self.getCpf(), self.getImdb_filme(), self.getSituacao(), self.getData_inicio(), self.getData_final())
        return all