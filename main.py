from typing import Union

from fastapi import FastAPI, Query
import requests
#https://fastapi.tiangolo.com/#alternative-api-docs-upgrade
app = FastAPI()


@app.get("/")
def read_root():
    '''
    Endpoint que exibe uma mensagem incrível no mundo da programação!
    '''
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante:str=Query(None)):
    '''
    Endpoint para ver os cardápios do restaurante!
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url=url) 
    
    if response.status_code == 200:
        json_data = response.json()

        if restaurante is None:
            return {"data":json_data}

        restaurant_data = []

        for item in json_data:

            if restaurante == item['Company']:
                
                restaurant_data.append({
                    "item":item["Item"],
                    "price":item["price"],
                    "description":item["description"],
                })
        return {"data":{
            "restaurante":restaurante,
            "cardapio":restaurant_data
        }}
    else:
        return {
            "error":f'error: {response.status_code} - {response.text}'
        }


#(venv) appuser@f72381e4309b:/app$ uvicorn main:app --host 0.0.0.0 --port 5000 --reload