import pytest
import requests
from urls import Urls
from data import Data
from api_methods import ApiMethods

@pytest.fixture
def create_user_account():
    response = ApiMethods.create_account(Data.EMAIL, Data.PASSWORD, Data.NAME)
    access_token = response.json().get('accessToken')
    yield access_token
    requests.delete(Urls.delete_user, headers={'Authorization': access_token})
