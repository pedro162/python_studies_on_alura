class Cliente:
    def __init__(self, nome, documento, telefone):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone

    

cliente = Cliente('Pedro', '61245584593', '9898475612')
print(cliente)