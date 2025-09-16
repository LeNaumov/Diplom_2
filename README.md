# Diplom_2## Дипломный проект. Задание 2: API

## Структура проекта

- `data.py` - содержит данные для тестов.
- `methods/order_methods` - методы для работы с заказом.
- `methods/user_methods` - методы для работы с пользователем.
- `tests/test_user.py` - тесты создания и авторизации пользователя.
- `tests/test_order.py` - тесты создания заказа.
- `conftest.py` - настройки и фикстуры для тестов.
- `allure-report/index.html` - allure отчёт о прогоне тестов.


## Инструкция по запуску:

### 1. Установите зависимости:

> pip install -r requirements.txt

### 2. Запустить все тесты и записать отчет:

> pytest --alluredir=./allure-results

### 3. Посмотреть отчет по прогону html

> allure serve ./allure-results
