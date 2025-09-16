from os import access
import allure
import requests
import data
import urls

class UserMethods:

    @staticmethod
    @allure.step("Создаём пользователя")
    def user_create(create_body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_CREATE}', json=create_body)

    @staticmethod
    @allure.step("Логинимся пользователем")
    def user_login(login_body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_LOGIN}', json=login_body)

    @staticmethod
    @allure.step("Удаляем пользователя")
    def user_delete(token):
        headers = {"Authorization": token}
        return requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

    @staticmethod
    @allure.step("Logout пользователя")
    def user_logout(logout_body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_LOGOUT}', json=logout_body)

    @staticmethod
    @allure.step("Получаем токен пользователя")
    def user_get_token(email, password):
        response =  requests.post(f'{urls.BASE_URL}{urls.USER_LOGIN}', json={
            'email': email,
            'password': password
        })
        access_token = response.json()["accessToken"].split(' ')[1]
        return access_token