from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import Locators
from helpers.data import Data

class TestLogoutOfAccount:
    def test_logout_of_account(self, driver, open_main_page):
        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Нажимаем кнопку "Личный кабинет" и ожидаем чтобы прогрузилась страница ЛК(кнопка "Профиль")
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))

        # Нажимаем кнопку "Выход" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.logout).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Проверяем что произошел выход на страницу авторизации
        current_url = driver.current_url
        assert current_url =='https://stellarburgers.nomoreparties.site/login'