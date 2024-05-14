import requests
from django.conf import settings


class CatRepository:
    def __init__(self, api: str = None) -> None:
        self._api = api


    def get_random_pic(self) -> str:
        response = requests.get(self._api)
        image = response.json()[0]['url']
        return image