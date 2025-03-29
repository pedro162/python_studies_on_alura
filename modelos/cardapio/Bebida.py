from modelos.cardapio.ItemCardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)