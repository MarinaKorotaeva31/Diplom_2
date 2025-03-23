import allure
import requests
from urls import Urls

class ApiMethods:
    @staticmethod
    @allure.step('Создание пользователя')
    def create_account(email: str, password: str, name: str):
        response = requests.post(url=Urls.create_user, json={"email": email, "password": password, "name": name})
        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_account(access_token: str):
        response = requests.delete(Urls.delete_user, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(email: str, password: str, name: str):
        response = requests.post(Urls.login_user, json={"email": email, "password": password, "name": name})
        return response

    @staticmethod
    @allure.step('Изменение данных пользователя с авторизацией')
    def change_user_data(payload, access_token: str):
        response = requests.patch(Urls.change_data, json=payload, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step('Изменение данных пользователя без авторизации')
    def change_user_data_unauthorized(payload):
        response = requests.patch(Urls.change_data, json=payload)
        return response

    @staticmethod
    @allure.step('Получение данных об ингредиентах')
    def get_ingredients():
        response = requests.get(Urls.get_ingredients)
        return response

    @staticmethod
    @allure.step('Создание заказа')
    def create_orders(payload, access_token: str):
        response = requests.post(Urls.create_orders, json=payload, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step('Получение заказа конкретного пользователя')
    def receiving_orders(access_token: str):
        response = requests.get(Urls.check_orders, headers={'Authorization': access_token})
        return response
