import allure
import random
from api_methods import ApiMethods
from data import Data

class TestCreateOrders:
    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Создается аккаунт и происходит авторизация, проверяется создание заказа с любым ингредиентом'
                        ' из имеющихся, проверяется статус-код и текст. Аккаунт удаляется.')
    def test_create_orders_authorized(self, create_user_account):
        access_token = create_user_account
        ingredients = {'ingredients':ApiMethods.get_ingredients().json()['data'][random.randint(0, 14)]['_id']}
        response = ApiMethods.create_orders(ingredients, access_token)
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text


    #  тест проходит, хотя не должен - внутренний баг
    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Проверяется создание заказа без авторизации с любым ингредиентом'
                        ' из имеющихся, проверяется статус-код и текст. Аккаунт удаляется.')
    def test_create_orders_unauthorized(self):
        ingredients = {'ingredients': ApiMethods.get_ingredients().json()['data'][random.randint(0, 14)]['_id']}
        response = ApiMethods.create_orders(ingredients, access_token='')
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text


    #  Проверка создания заказа с ингредиентами прошла в первых двух тестах. Излишне писать ещё одну проверку.


    @allure.title('Проверка возможности создания заказа с пустым списком ингредиентов')
    @allure.description('Создаётся пустой словарь ингредиентов, передающийся в метод для запроса'
                        ' на создание заказа. Проверяется код и ответ ошибки')
    def test_create_orders_without_ingredients(self, create_user_account):
        access_token = create_user_account
        ingredients = {}
        response = ApiMethods.create_orders(ingredients, access_token=access_token)
        assert response.status_code == 400 and Data.CODE_400_BAD_REQUEST in response.text


    @allure.title('Проверка возможности создания заказа с неверным хэшем')
    @allure.description('В методом на создание заказа отправляется словарь с неверным хэшем, проверяется код и текст ошибки')
    def test_create_orders_wrong_id(self, create_user_account):
        access_token = create_user_account
        ingredients = {'ingredients':f'{random.randint(1, 1000000)}'}
        response = ApiMethods.create_orders(ingredients, access_token=access_token)
        assert response.status_code == 500 and Data.CODE_500 in response.text
