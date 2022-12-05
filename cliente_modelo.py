class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco_rua, endereco_numero, endereco_bairro, telefone,  email):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._endereco_rua = endereco_rua
        self._endereco_numero = endereco_numero
        self._endereco_bairro = endereco_bairro
        self._telefone = telefone
        self._email = email
        self._situacao = '1'
    
    def setCpf(self, cpf): self._cpf = cpf
    def setNome(self, nome): self._nome = nome
    def setData_nascimento(self, data_nascimento): self._data_nascimento = data_nascimento
    def setEndereco_rua(self, endereco_rua): self._endereco_rua = endereco_rua
    def setEndereco_numero(self, endereco_numero): self._endereco_numero = endereco_numero
    def setEndereco_bairo(self, endereco_bairo): self._endereco_bairro = endereco_bairo
    def setTelefone(self, telefone): self._telefone = telefone
    def setEmail(self, email): self._email = email
    def setSituacao(self, situacao): self._situacao = situacao

    def getCpf(self): return self._cpf
    def getNome(self): return self._nome
    def getData_nascimento(self): return self._data_nascimento
    def getEndereco_rua(self): return self._endereco_rua
    def getEndereco_numero(self): return self._endereco_numero
    def getEndereco_bairo(self): return self._endereco_bairro
    def getTelefone(self): return self._telefone
    def getEmail(self): return self._email
    def getSituacao(self): return self._situacao
    def getAll(self):
        all = (self.getCpf(), self.getNome(), self.getData_nascimento(), self.getEndereco_rua(), self.getEndereco_numero(), self.getEndereco_bairo(), self.getTelefone(), self.getEmail(), self.getSituacao())
        return all