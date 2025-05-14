import requests


class CarApi:

    def __init__(self):
        self.__base_url = "http://localhost:8000"

    def get_cars(self):
        response = requests.get(url=f"{self.__base_url}/cars")
        return response.json()
