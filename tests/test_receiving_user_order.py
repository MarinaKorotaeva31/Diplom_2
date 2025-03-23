import allure
from data import Data
from api_methods import ApiMethods

class TestReceivingUserOrder:
    @allure.title('Проверка получение заказов конкретного пользователя с авторизацией')
    @allure.title('Осуществляется создание и вход в аккаунт, эти данные передаются в метод получения информации о заказах,'
                  ' проверяется статус-код и текст ответа')
    def test_receiving_order_authorized(self, create_user_account):
        access_token = create_user_account
        response = ApiMethods.receiving_orders(access_token)
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text


    @allure.title('Проверка получение заказов конкретного пользователя без авторизации')
    @allure.title(
        'Происходит обращение к методу получения информации о заказах без предварительной авторизации,'
        ' проверяется статус-код и текст ответа ошибки')
    def test_receiving_order_unauthorized(self):
        response = ApiMethods.receiving_orders(access_token='')
        assert response.status_code == 401 and Data.CODE_401_NO_TOKEN
