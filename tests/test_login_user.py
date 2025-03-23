import allure
import pytest
import requests
from urls import Urls
from data import Data
from api_methods import ApiMethods


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Создается аккаунт, осуществляется вход, проверяется статус-код запроса и текст. Удаляется аккаунт.')
    def test_login_existing_user_is_success(self, create_user_account):
        response = ApiMethods.login_user(Data.EMAIL, Data.PASSWORD, Data.NAME)
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text

    @allure.title('Проверка невозможности входа при вводе неверного логина')
    @allure.description('Осуществляется вход с изменённым или пустыми email и паролем, проверяется статус-код и текст ответа')
    @pytest.mark.parametrize(
        'payload',
        [
            ({"email":f'{Data.EMAIL}123', "password":Data.PASSWORD, "name":Data.NAME}),
            ({"email":Data.EMAIL, "password":f'{Data.PASSWORD}123', "name":Data.NAME}),
            ({"password": Data.PASSWORD, "name": Data.NAME}),
            ({"email": Data.EMAIL, "name": Data.NAME}),
        ]
    )
    def test_login_wrong_data_is_fall(self, payload):
        response = requests.post(Urls.login_user, json=payload)
        assert response.status_code == 401 and response.text == Data.CODE_401_UNAUTHORIZED
