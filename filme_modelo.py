class Filme:
    def __init__(self, imdb, titulo_or, titulo_br, ano, duracao_min, idioma, genero, direcao, roteiro, classificacao, pais):
        self._titutlo_or = titulo_or
        self._titutlo_br = titulo_br
        self._ano = ano
        self._duracao_min = duracao_min
        self._idioma = idioma
        self._genero = genero
        self._direcao = direcao
        self._roteiro = roteiro
        self._imdb = imdb
        self._classificacao = classificacao
        self._pais = pais
        self._disponibilidade = 1

    def setTitulo_or(self, titulo_or): self._titutlo_or = titulo_or
    def setTitulo_br(self, titulo_br): self._titutlo_br = titulo_br
    def setAno(self, ano): self._ano = ano
    def setDuracao(self, minutos): self._duracao_min = minutos
    def setIdioma(self, idioma): self._idioma = idioma
    def setGenero(self, genero): self._genero = genero
    def setDirecao(self, direcao): self._direcao = direcao
    def setRoteiro(self, roteiro): self._roteiro = roteiro
    def setImdb(self, imdb): self._imdb = imdb
    def setClassificacao(self, classificacao): self._classificacao = classificacao
    def setPais(self, pais): self._pais = pais
    def setDisponibilidade(self, disponibilidade): self._disponibilidade = disponibilidade

    def getTitulo_or(self): return self._titutlo_or
    def getTitulo_br(self): return self._titutlo_br
    def getAno(self): return self._ano
    def getDuracao(self): return self._duracao_min
    def getIdioma(self): return self._idioma
    def getGenero(self): return self._genero
    def getDirecao(self): return self._direcao
    def getRoteiro(self): return self._roteiro
    def getImdb(self): return self._imdb
    def getClassificacao(self): return self._classificacao
    def getPais(self): return self._pais
    def getDisponibilidade(self): return self._disponibilidade

    def getAll(self):
        all = (self.getImdb(), self.getTitulo_or(), self.getTitulo_br(), self.getAno(), self.getDuracao(), self.getIdioma(), self.getGenero(), self.getDirecao(), self.getRoteiro(), self.getClassificacao(), self.getPais(), self.getDisponibilidade())
        return all
