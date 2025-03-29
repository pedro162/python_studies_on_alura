from __future__ import annotations
class Avaliacao:
    def __init__(self, cliente:"Pessoa", nota:float):
        self._cliente = cliente
        self._nota = nota

    def __str__(self):
        return f'Cliente: {self._cliente.nome}, Nota: {self._nota}'

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def nota(self):
        return self._nota