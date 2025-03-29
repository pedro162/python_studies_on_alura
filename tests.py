from __future__ import annotations
from modelos.pessoa import Pessoa
from modelos.conta_bancaria import ContaBancaria
from modelos.avaliacao import Avaliacao
from modelos.restaurante_estudo import RestauranteEstudo
import random

#Testing the class
pessoa_joao = Pessoa('João', 30, 'Engenheiro')
conta = ContaBancaria(pessoa_joao, 1000.0)
conta.ativo = True
print(conta)
pessoa_maria = Pessoa('Maria', 25, 'Médica')
conta = ContaBancaria(pessoa_maria, 2000.0)
print(conta)

avaliacao_maria = Avaliacao(pessoa_maria, random.uniform(0, 10))
avaliacao_joao = Avaliacao(pessoa_joao, random.uniform(0, 10))
restaurante = RestauranteEstudo('Pizzaria', 'Italiana')
restaurante.ativo = True
restaurante.receber_avaliacao(avaliacao_maria)
restaurante.receber_avaliacao(avaliacao_joao)

avaliacao_maria = Avaliacao(pessoa_maria, random.uniform(0, 10))
avaliacao_joao = Avaliacao(pessoa_joao, random.uniform(0, 10))
restaurante = RestauranteEstudo('Pizzaria', 'Italiana')
restaurante.ativo = True
restaurante.receber_avaliacao(avaliacao_maria)
restaurante.receber_avaliacao(avaliacao_joao)

restaurante.listar_restaurantes()