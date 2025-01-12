from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import Locators
from helpers.data import Data

class TestLoginInAccount:
    def test_login_in_account_by_button_sign_in_account(self, driver, open_main_page):
        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Проверяем что произошел вход(появилась кнопка "Оформить заказ")
        assert len(driver.find_elements(*Locators.place_an_order)) == 1

    def test_login_in_account_by_button_personal_account(self, driver, open_main_page):
        #  Нажимаем "Личный кабинет" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Проверяем что произошел вход(появилась кнопка "Оформить заказ")
        assert len(driver.find_elements(*Locators.place_an_order)) == 1

    def test__login_in_account_by_registration_form(self, driver):
        #Открываем страницу регистрации
        driver.get('https://stellarburgers.nomoreparties.site/register')

        #  Нажимаем "Войти" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Проверяем что произошел вход(появилась кнопка "Оформить заказ")
        assert len(driver.find_elements(*Locators.place_an_order)) == 1

    def test__login_in_account_by_forgot_password_form(self, driver):
        #Открываем страницу восстановления пароля
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        #  Нажимаем "Войти" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Проверяем что произошел вход(появилась кнопка "Оформить заказ")
        assert len(driver.find_elements(*Locators.place_an_order)) == 1

