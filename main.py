from flask import Flask
from Service.mercadolibreAPI import MercadoLibre
from Database.rabbit import Rabbit
app = Flask(__name__)


@app.route("/get_list_itens/")
def get_list_itens():
    try:
        response = MercadoLibre.get_list_itens()
        return response
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}


@app.route("/get_item_information/<item>")
def get_item_information(item):
    try:
        response = MercadoLibre.get_item_information(item)
        Rabbit.addinformation(response)
        return "Item saved"
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
