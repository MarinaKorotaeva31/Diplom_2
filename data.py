class Data:
    #  параметры для регистрации
    EMAIL = 'user3215@yandex.ru'
    PASSWORD = 'paSSword_for_user_3214'
    NAME = 'user3124'

    #  ответы на запросы
    CODE_200_TEXT = '"success":true'
    CODE_400_BAD_REQUEST = '{"success":false,"message":"Ingredient ids must be provided"}'
    CODE_401_UNAUTHORIZED = '{"success":false,"message":"email or password are incorrect"}'
    CODE_401_NO_TOKEN = '{"success":false,"message":"You should be authorised"}'
    CODE_403_EXISTING = '{"success":false,"message":"User already exists"}'
    CODE_403_EMPTY_FIELD = '{"success":false,"message":"Email, password and name are required fields"}'
    CODE_500 = 'Internal Server Error'
