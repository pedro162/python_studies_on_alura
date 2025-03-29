from __future__ import annotations
from modelos.pessoa import Pessoa
from modelos.conta_bancaria import ContaBancaria

#Testing the class
pessoa = Pessoa('João', 30, 'Engenheiro')
conta = ContaBancaria(pessoa, 1000.0)
conta.ativo = True
print(conta)
pessoa = Pessoa('Maria', 25, 'Médica')
conta = ContaBancaria(pessoa, 2000.0)
print(conta)