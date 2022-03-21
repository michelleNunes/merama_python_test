import requests
from requests.adapters import HTTPAdapter

class MercadoLibre(object):

    @staticmethod
    def get_list_itens():
        session = requests.Session()
        session.mount("http://", HTTPAdapter(max_retries=3))

        url = f"https://api.mercadolibre.com/users/$USER_ID/items/search?search_type=scan"
        response = session.get(url)
        result_information = response.json()
        return result_information

    @staticmethod
    def get_item_information(item_id):
        session = requests.Session()
        session.mount("http://", HTTPAdapter(max_retries=3))

        url = f"https://api.mercadolibre.com/items/{item_id}"
        response = session.get(url)
        result_information = response.json()

        return result_information
