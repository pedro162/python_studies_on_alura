class RestauranteEstudo:
    restaurants = []

    def __init__(self, nome, categoria):
        self.__nome = nome.title()
        self.__categoria = categoria.upper()
        self.__ativo = False
        RestauranteEstudo.restaurants.append(self)

    def __str__(self):
        return {"nome":self.__nome, "categoria":self.__categoria, 'ativo': self.ativo}
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurants:
            print(f'{restaurante.__nome.ljust(25)} | {restaurante.__categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        #this is a comment
        #return '☑' if self.__ativo else '☐'#this is a comment
        return '☑' if self.__ativo else '☐'#this is a comment
    
    @ativo.setter
    def ativo(self, valor):
        if isinstance(valor, bool):
            self.__ativo = valor
        else:
            raise ValueError('O valor deve ser um booleano (True ou False)')
        
    def alternar_estado(self):
        self.__ativo = not self.__ativo
        

restaurante = RestauranteEstudo('Restaurante popular', 'popular').ativo = True
restaurante = RestauranteEstudo('Restaurante gourmet', 'gourmet')
restaurante.listar_restaurantes()
#print(vars(restaurante))
#print(dir(restaurante))
#x, y, z = 'Orange', 'Banana', 'Cherry'
#print(x, y, z)
#x = y = z = "Orange"
#print(x, y, z)

#https://www.w3schools.com/python/python_datatypes.asp
#Getting the Data Type
