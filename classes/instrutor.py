class Instrutor:

  def __init__(self, nome, sobrenome, data_nascimento, endereco, telefone, id = None):
    self.nome = nome
    self.id = id
    self.sobrenome = sobrenome
    self.data_nascimento = data_nascimento
    self.endereco = endereco
    self.telefone = telefone