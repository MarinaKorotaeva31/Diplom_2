import allure
import pytest
from data import Data
from api_methods import ApiMethods


class TestChangeUserData:
    @allure.title('Изменение данных пользователя с авторизацией')
    @allure.description('Используется фикстура для создания аккаунта и входа в него, изменяются данные на'
                        ' указанные в параметризации, проверяется статус-код и текст. Аккаунт удаляется.')
    @pytest.mark.parametrize(
        'changed_data',
        [
            ({"email":f'{Data.EMAIL}123', "password":Data.PASSWORD, "name":Data.NAME}),
            ({"email":Data.EMAIL, "password":f'{Data.PASSWORD}123', "name":Data.NAME}),
            ({"email":Data.EMAIL, "password":Data.PASSWORD, "name":f'{Data.NAME}123'})
        ]
    )
    def test_change_data_authorized(self, create_user_account, changed_data):
        access_token = create_user_account
        response = ApiMethods.change_user_data(changed_data, access_token)
        assert response.status_code == 200 and Data.CODE_200_TEXT in response.text

    @allure.title('Изменение данных пользователя без авторизации')
    @allure.description('Используется фикстура для создания аккаунта, попытка изменения данных на указанные'
                        ' в параметризации, проверяется статус-код и текст ошибки. Аккаунт удаляется.')
    @pytest.mark.parametrize(
        'changed_data',
        [
            ({"email": f'{Data.EMAIL}123', "password": Data.PASSWORD, "name": Data.NAME}),
            ({"email": Data.EMAIL, "password": f'{Data.PASSWORD}123', "name": Data.NAME}),
            ({"email": Data.EMAIL, "password": Data.PASSWORD, "name": f'{Data.NAME}123'})
        ]
    )
    def test_change_data_unauthorized(self, create_user_account, changed_data):
        response = ApiMethods.change_user_data_unauthorized(changed_data)
        assert response.status_code == 401 and response.text == Data.CODE_401_NO_TOKEN
