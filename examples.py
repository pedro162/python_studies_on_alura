from modelos.restaurante import Restaurante
from modelos.cardapio.Bebida import Bebida
from modelos.cardapio.Prato import Prato
import time
import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url=url) 
print(response)

if response.status_code == 200:
    json_data = response.json()
    restaurant_data = {}

    for item in json_data:
        restaurant_name = item['Company']

        if(restaurant_name not in restaurant_data):
            restaurant_data[restaurant_name] = []
        
        restaurant_data[restaurant_name].append({
            "item":item["Item"],
            "price":item["price"],
            "description":item["description"],
        })
    
    for restaurant_name, data in restaurant_data.items():
        filename = f"./resources/restaurant/{restaurant_name}.json"
        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
            pass
else:
    print(f"O erro foi {response.status_code}")

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
#https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json
#pip install -r requirements.txt 
#https://economia.awesomeapi.com.br/last/USD-BRL#API com dados de dollar e real

def main():
    restaurante_praca.exibir_cardapio

     # Manter o container em execução
    while True:
        time.sleep(100)

if __name__ == '__main__':
    main()