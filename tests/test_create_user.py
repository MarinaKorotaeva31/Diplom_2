import allure
import pytest
import requests
from urls import Urls
from data import Data
from api_methods import ApiMethods

class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Создаётся аккаунт, проверяет статус-код и текст ответа об успешном создании, осуществляется получение токена. После аккаунт удаляется.')
    def test_create_unique_user_is_success(self):
        response = ApiMethods.create_account(Data.EMAIL, Data.PASSWORD, Data.NAME)
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text
        access_token = response.json()['accessToken']
        ApiMethods.delete_account(access_token)

    @allure.title('Проверка невозможности создания существующего аккаунта')
    @allure.description(
        'С помощью фикстуры создаётся аккаунт, после чего повторяется попытка создания курьера с теми же данными. Проверяется статус-код и текст ответа'
        'и тело ответа. Аккаунт удаляется')
    def test_create_duplicate_account_is_fall(self, create_user_account):
        response = ApiMethods.create_account(Data.EMAIL, Data.PASSWORD, Data.NAME)
        assert response.status_code == 403 and response.text == Data.CODE_403_EXISTING

    @allure.title('Проверка невозможности создания аккаунта без обязательного параметра')
    @allure.description('Создаётся аккаунт без передачи параметра "email", "пароль" и "имя", проверяется статус-код и текст ответа')
    @pytest.mark.parametrize(
        'payload',
        [
            ({"password":Data.PASSWORD, "name":Data.NAME}),
            ({"email":Data.EMAIL, "name":Data.NAME}),
            ({"email":Data.EMAIL, "password":Data.PASSWORD})
        ]
    )
    def test_create_account_empty_field_is_fall(self, payload):
        response = requests.post(url=Urls.create_user, json=payload)
        assert response.status_code == 403 and response.text == Data.CODE_403_EMPTY_FIELD
