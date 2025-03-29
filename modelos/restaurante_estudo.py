from __future__ import annotations
from modelos.avaliacao import Avaliacao
class RestauranteEstudo:
    """Representa um restaurante e suas características."""
    restaurants = []

    def __init__(self, nome, categoria):

        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """

        self.__nome = nome.title()
        self.__categoria = categoria.upper()
        self.__ativo = False
        self.__avaliacao = []
        RestauranteEstudo.restaurants.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f"nome {self.__nome}, categoria: {self.__categoria}, ativo: {self.ativo}, media avaliacao: {self.media_avaliacao}"
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""

        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurants:
            print(f'{restaurante.__nome.ljust(25)} | {restaurante.__categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""

        #this is a comment
        #return '☑' if self.__ativo else '☐'#this is a comment
        return '☑' if self.__ativo else '☐'#this is a comment
    
    @ativo.setter
    def ativo(self, valor):
        """
        Define o estado de atividade do restaurante.
        Parâmetros:
        - valor (bool): O estado de atividade (True ou False).
        """

        if isinstance(valor, bool):
            self.__ativo = valor
        else:
            raise ValueError('O valor deve ser um booleano (True ou False)')
        
    def alternar_estado(self):
        """
        Alterna o estado de atividade do restaurante entre ativo e inativo.
        """
        self.__ativo = not self.__ativo

    @property
    def nome(self):
        """Retorna o nome do restaurante."""
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """
        Define o nome do restaurante.
        Parâmetros:
        - nome (str): O novo nome do restaurante.
        """

        if isinstance(nome, str):
            self.__nome = nome.title()
        else:
            raise ValueError('O nome deve ser uma string')
        
    @property
    def categoria(self):
        """Retorna a categoria do restaurante."""
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        """
        Define a categoria do restaurante.
        Parâmetros:
        - categoria (str): A nova categoria do restaurante.
        """

        if isinstance(categoria, str):
            self.__categoria = categoria.upper()
        else:
            raise ValueError('A categoria deve ser uma string')
        
    @property
    def avaliacao(self):
        """Retorna a lista de avaliações do restaurante."""
        return self.__avaliacao
    
    @avaliacao.setter
    def avaliacao(self, avaliacao):
        """
        Define a lista de avaliações do restaurante.
        Parâmetros:
        - avaliacao (list): Uma lista de instâncias da classe Avaliacao.
        """

        if isinstance(avaliacao, list):
            self.__avaliacao = avaliacao
        else:
            raise ValueError('A avaliação deve ser uma lista')
       
    def receber_avaliacao(self, avaliacao:Avaliacao):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - avaliacao (Avaliacao): Uma instância da classe Avaliacao.
        """

        if isinstance(avaliacao, Avaliacao):
            self.__avaliacao.append(avaliacao)
        else:
            raise ValueError('A avaliação deve ser uma instância da classe Avaliacao')
    
    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self.__avaliacao:
            return 0
        
        return round(sum(avaliacao.nota for avaliacao in self.__avaliacao) / len(self.__avaliacao),1)