from __future__ import annotations
from typing import Optional

class Pessoa:
    def __init__(self, nome:str, idade:int, profissao:str, conta:Optional["ContaBancaria"] = None):
        self.__nome = nome.title()
        self.__idade = idade
        self.__profissao = profissao.title()
        self.__conta = conta

    def __str__(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}, Profissão: {self.__profissao}'
    
    @property
    def saudacao(self):
        return f'Olá, meu nome é {self.__nome} e tenho {self.__idade} anos. Sou {self.__profissao}'
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property 
    def profissao(self):
        return self.__profissao
    
    @property
    def conta(self):
        return self.__conta

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nome = valor.title()
        else:
            raise ValueError('O nome deve ser uma string não vazia')
    
    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__idade = valor
        else:
            raise ValueError('A idade deve ser um número inteiro não negativo')

    @profissao.setter
    def profissao(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__profissao = valor.title()
        else:
            raise ValueError('A profissão deve ser uma string não vazia')
        
    @conta.setter
    def conta(self, valor):
        if isinstance(valor, ContaBancaria):
            self.__conta = valor
        else:
            raise ValueError('A conta deve ser uma instância da classe ContaBancaria')

    def aniversario(self):
        self.__idade += 1
    