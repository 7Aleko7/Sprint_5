import random

class Data:
    # Авторизационные данные тестового пользователя
    test_user_mail='1@test.ru'
    test_user_password=123321

    def random_email():
        mail= f"ivanov_alexandr{random.randint(100, 999)}@yandex.com"
        return mail

    def random_password():
        password= random.randint(100000, 999999999)
        return password