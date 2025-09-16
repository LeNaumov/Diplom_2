import pytest
import requests
import allure
import generators
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def create_user_and_delete():
    with allure.step('Получаем сгенерированные данные пользователя'):
        user_data = generators.generate_user_body()
    name = user_data['name']
    password = user_data['password']
    email = user_data['email']
    with allure.step(f'Создаём пользователя с данными: {user_data}'):
        response = UserMethods.user_create(user_data)
    access_token = UserMethods.user_get_token(email, password)
    user_data["access_token"] = access_token

    yield user_data

    with allure.step('Удаляем созданного пользователя'):
        UserMethods.user_delete(access_token)

@pytest.fixture()
def create_user_data_and_delete():
    with allure.step('Получаем сгенерированные данные курьера'):
        user_register_body = generators.generate_user_body()
        email = user_register_body['email']
        password = user_register_body['password']

        user_login_body = {'email': email, 'password': password}
    yield [user_register_body, user_login_body, email, password]
    
    with allure.step('Логинимся в систему созданным курьером'):
        user = UserMethods.user_login(user_login_body)
        token = user.json().get("accessToken")

    with allure.step('Удаляем созданного курьера'):
        UserMethods.user_delete(token)


@pytest.fixture()
def create_and_cancel_order():

    created_tracks = []

    def _create_order(order_data):
        with allure.step('Создаём новый заказ'):
            response = OrderMethods.order_create(order_data)
        order_track = response.json()['track']
        created_tracks.append(order_track)
        return response

    yield _create_order

    with allure.step('Удаляем созданные заказы'):
        for track in created_tracks:
            OrderMethods.order_cancel(track)