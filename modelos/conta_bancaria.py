from __future__ import annotations
from typing import Optional

class ContaBancaria:
    def __init__(self, titular:"Pessoa", saldo:float):
        self.__titular = titular
        self.__saldo = saldo
        self.__ativo = False
        
    def __str__(self):
        return f'Titular: {self.__titular.nome}, Saldo: {self.__saldo}, Ativo: {"Sim" if self.__ativo else "Não"}'
    
    @property
    def ativo(self):
        return self.__ativo
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError('O saldo deve ser um número positivo')
        
    @titular.setter
    def titular(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titular = valor.title()
        else:
            raise ValueError('O titular deve ser uma string não vazia')
    
    @ativo.setter
    def ativo(self, valor):
        if isinstance(valor, bool):
            self.__ativo = valor
        else:
            raise ValueError('O valor deve ser um booleano (True ou False)')
    
    @classmethod
    def ativar_cotna(cls, conta):
        conta.ativo = True