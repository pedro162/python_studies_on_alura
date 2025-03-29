from modelos.restaurante import Restaurante
from modelos.cardapio.Bebida import Bebida
from modelos.cardapio.Prato import Prato
import time
import requests
import json

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
#https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json

def main():
    restaurante_praca.exibir_cardapio

     # Manter o container em execução
    while True:
        time.sleep(100)

if __name__ == '__main__':
    main()